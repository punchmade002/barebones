-- Run this once in the Supabase SQL editor, after schema.sql.
--
-- Problem it fixes: a profile row (and so the username) is created the moment
-- someone signs up, before they confirm their email. If the confirmation email
-- never arrives, or they typo their address, that username is stuck forever and
-- every retry fails with "That username is already taken."
--
-- After this:
--   * the same email can retry with the same username (Supabase re-sends the
--     confirmation email instead of creating a second account);
--   * a username held by a sign-up that was never confirmed within 24 hours is
--     released, and that abandoned, unconfirmed auth user is removed when
--     someone else claims the name. Unconfirmed users never had a session, so
--     they have no study data to lose.

create or replace function public.username_claimable(candidate text, candidate_email text)
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
      from public.profiles p
      join auth.users u on u.id = p.id
      where p.username = lower(candidate)
        and not (
          u.email_confirmed_at is null
          and (
            lower(u.email) = lower(trim(candidate_email))
            or u.created_at < now() - interval '24 hours'
          )
        )
    );
$$;

revoke all on function public.username_claimable(text, text) from public;
grant execute on function public.username_claimable(text, text) to anon, authenticated;

-- Same rule as username_claimable, applied server-side so the profile insert
-- below can never collide with an abandoned sign-up.
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

  delete from auth.users u
  using public.profiles p
  where p.id = u.id
    and p.username = requested_username
    and u.id <> new.id
    and u.email_confirmed_at is null
    and u.created_at < now() - interval '24 hours';

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
