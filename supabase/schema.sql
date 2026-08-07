-- Run this once in the Supabase SQL editor.
-- It creates identity-linked profiles, cloud study state, and a payment-ready
-- entitlement boundary. Client users can never grant themselves paid access.

create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  username text not null unique check (username = lower(username)),
  account_origin text not null default 'self_service'
    check (account_origin in ('self_service', 'legacy_migration', 'admin')),
  created_at timestamptz not null default now()
);

create table if not exists public.study_states (
  user_id uuid primary key references auth.users(id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

-- Account emails are copied here at account creation so administrators can
-- export a deduplicated mailing list without exposing auth.users to browsers.
create table if not exists public.mailing_list (
  user_id uuid primary key references auth.users(id) on delete cascade,
  email text not null unique check (email = lower(trim(email)) and email <> ''),
  account_origin text not null default 'self_service'
    check (account_origin in ('self_service', 'legacy_migration', 'admin')),
  created_at timestamptz not null default now()
);

create table if not exists public.entitlements (
  user_id uuid not null references auth.users(id) on delete cascade,
  product_key text not null,
  status text not null
    check (status in ('trialing', 'active', 'past_due', 'canceled', 'expired')),
  current_period_end timestamptz,
  updated_at timestamptz not null default now(),
  primary key (user_id, product_key)
);

-- Payment-provider identifiers stay out of the browser-readable public schema.
create schema if not exists private;

create table if not exists private.billing_customers (
  user_id uuid primary key references auth.users(id) on delete cascade,
  provider text not null default 'stripe',
  provider_customer_id text not null unique,
  provider_subscription_id text unique,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table public.profiles enable row level security;
alter table public.study_states enable row level security;
alter table public.mailing_list enable row level security;
alter table public.entitlements enable row level security;

drop policy if exists "Read own profile" on public.profiles;
create policy "Read own profile"
  on public.profiles for select
  to authenticated
  using ((select auth.uid()) = id);

drop policy if exists "Read own study state" on public.study_states;
create policy "Read own study state"
  on public.study_states for select
  to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "Insert own study state" on public.study_states;
create policy "Insert own study state"
  on public.study_states for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists "Update own study state" on public.study_states;
create policy "Update own study state"
  on public.study_states for update
  to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

drop policy if exists "Read own entitlements" on public.entitlements;
create policy "Read own entitlements"
  on public.entitlements for select
  to authenticated
  using ((select auth.uid()) = user_id);

-- Mailing-list rows contain customer contact data. There is intentionally no
-- browser policy: only the service role may export them.
revoke all on public.mailing_list from anon, authenticated;
grant select on public.mailing_list to service_role;

-- The browser can read its entitlement, but only a trusted webhook/server using
-- Supabase's secret key may insert, update, or delete entitlement rows.
revoke insert, update, delete on public.entitlements from anon, authenticated;
revoke all on table private.billing_customers from anon, authenticated;
grant usage on schema private to service_role;
grant all on table private.billing_customers to service_role;
grant all on table public.entitlements to service_role;

create or replace function public.username_available(candidate text)
returns boolean
language sql
security definer
set search_path = ''
stable
as $$
  select
    candidate ~ '^[A-Za-z0-9_-]{3,24}$'
    and not exists (
      select 1
      from public.profiles
      where username = lower(candidate)
    );
$$;

revoke all on function public.username_available(text) from public;
grant execute on function public.username_available(text) to anon, authenticated;

create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = ''
as $$
declare
  requested_username text;
  requested_origin text;
begin
  requested_username := lower(trim(new.raw_user_meta_data ->> 'username'));
  requested_origin := coalesce(new.raw_user_meta_data ->> 'account_origin', 'self_service');

  if requested_username !~ '^[a-z0-9_-]{3,24}$' then
    raise exception 'Username must be 3-24 characters using letters, numbers, _ or -';
  end if;

  if requested_origin not in ('self_service', 'legacy_migration', 'admin') then
    requested_origin := 'self_service';
  end if;

  insert into public.profiles (id, username, account_origin)
  values (new.id, requested_username, requested_origin);

  insert into public.study_states (user_id, data)
  values (new.id, '{}'::jsonb);

  if new.email is not null and trim(new.email) <> '' then
    insert into public.mailing_list (user_id, email, account_origin, created_at)
    values (
      new.id,
      lower(trim(new.email)),
      requested_origin,
      coalesce(new.created_at, now())
    )
    on conflict (user_id) do update
      set email = excluded.email,
          account_origin = excluded.account_origin;
  end if;

  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Applying this schema to an existing project also captures accounts that were
-- created before the mailing-list table existed.
insert into public.mailing_list (user_id, email, account_origin, created_at)
select
  id,
  lower(trim(email)),
  case
    when raw_user_meta_data ->> 'account_origin'
      in ('self_service', 'legacy_migration', 'admin')
      then raw_user_meta_data ->> 'account_origin'
    else 'self_service'
  end,
  created_at
from auth.users
where email is not null and trim(email) <> ''
on conflict (user_id) do update
  set email = excluded.email,
      account_origin = excluded.account_origin;

grant select on public.profiles to authenticated;
grant select, insert, update on public.study_states to authenticated;
grant select on public.entitlements to authenticated;
