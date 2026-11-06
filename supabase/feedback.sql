-- Feedback inbox. Run this in the Supabase SQL editor after schema.sql.
-- Safe to re-run.
--
-- Students submit feedback from the profile menu. An admin marks each item
-- addressed, optionally with a reply; the reply pops up for the student the
-- next time they open the app, once, and is then marked seen.
--
-- After running, make yourself an admin (swap in your username):
--   insert into public.admins (user_id)
--   select id from public.profiles where username = 'gabriel'
--   on conflict do nothing;

create table if not exists public.admins (
  user_id uuid primary key references auth.users(id) on delete cascade,
  created_at timestamptz not null default now()
);

alter table public.admins enable row level security;
-- No browser policy: admins are granted from the SQL editor only.
revoke all on public.admins from anon, authenticated;

create or replace function public.is_admin()
returns boolean
language sql
security definer
set search_path = ''
stable
as $$
  select exists (
    select 1 from public.admins where user_id = (select auth.uid())
  );
$$;

revoke all on function public.is_admin() from public;
grant execute on function public.is_admin() to authenticated;

create table if not exists public.feedback (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  username text not null,
  message text not null
    check (char_length(btrim(message)) between 1 and 4000),
  status text not null default 'open'
    check (status in ('open', 'addressed')),
  reply text check (reply is null or char_length(reply) <= 4000),
  addressed_at timestamptz,
  reply_seen_at timestamptz,
  created_at timestamptz not null default now()
);

create index if not exists feedback_user_unseen_idx
  on public.feedback (user_id)
  where status = 'addressed' and reply is not null and reply_seen_at is null;

create index if not exists feedback_created_idx
  on public.feedback (created_at desc);

alter table public.feedback enable row level security;

-- Students read their own feedback (to fetch unseen replies); admins read all.
drop policy if exists "Read own or admin feedback" on public.feedback;
create policy "Read own or admin feedback"
  on public.feedback for select
  to authenticated
  using ((select auth.uid()) = user_id or (select public.is_admin()));

-- All writes go through the functions below so a student can never edit a
-- reply, change status, or post under someone else's name.
revoke all on public.feedback from anon, authenticated;
grant select on public.feedback to authenticated;

create or replace function public.submit_feedback(feedback_message text)
returns uuid
language plpgsql
security definer
set search_path = ''
as $$
declare
  author_id uuid := auth.uid();
  author_name text;
  new_id uuid;
begin
  if author_id is null then
    raise exception 'Sign in to send feedback.';
  end if;
  if feedback_message is null or char_length(btrim(feedback_message)) = 0 then
    raise exception 'Feedback cannot be empty.';
  end if;
  if char_length(feedback_message) > 4000 then
    raise exception 'Feedback must be 4000 characters or fewer.';
  end if;

  -- Light flood guard: at most 10 messages per student per hour.
  if (
    select count(*) from public.feedback
    where user_id = author_id and created_at > now() - interval '1 hour'
  ) >= 10 then
    raise exception 'You have sent a lot of feedback recently. Try again in a little while.';
  end if;

  select username into author_name from public.profiles where id = author_id;

  insert into public.feedback (user_id, username, message)
  values (author_id, coalesce(author_name, 'unknown'), btrim(feedback_message))
  returning id into new_id;

  return new_id;
end;
$$;

create or replace function public.address_feedback(feedback_id uuid, reply_text text)
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare
  cleaned text := nullif(btrim(coalesce(reply_text, '')), '');
begin
  if not public.is_admin() then
    raise exception 'Only admins can address feedback.';
  end if;

  update public.feedback
    set status = 'addressed',
        reply = cleaned,
        addressed_at = now(),
        -- A new or changed reply should pop up again.
        reply_seen_at = null
    where id = feedback_id;

  if not found then
    raise exception 'That feedback no longer exists.';
  end if;
end;
$$;

create or replace function public.reopen_feedback(feedback_id uuid)
returns void
language plpgsql
security definer
set search_path = ''
as $$
begin
  if not public.is_admin() then
    raise exception 'Only admins can reopen feedback.';
  end if;

  update public.feedback
    set status = 'open',
        reply = null,
        addressed_at = null,
        reply_seen_at = null
    where id = feedback_id;
end;
$$;

create or replace function public.mark_feedback_replies_seen(feedback_ids uuid[])
returns void
language sql
security definer
set search_path = ''
as $$
  update public.feedback
    set reply_seen_at = now()
    where id = any(feedback_ids)
      and user_id = (select auth.uid())
      and reply_seen_at is null;
$$;

revoke all on function public.submit_feedback(text) from public;
revoke all on function public.address_feedback(uuid, text) from public;
revoke all on function public.reopen_feedback(uuid) from public;
revoke all on function public.mark_feedback_replies_seen(uuid[]) from public;
grant execute on function public.submit_feedback(text) to authenticated;
grant execute on function public.address_feedback(uuid, text) to authenticated;
grant execute on function public.reopen_feedback(uuid) to authenticated;
grant execute on function public.mark_feedback_replies_seen(uuid[]) to authenticated;
