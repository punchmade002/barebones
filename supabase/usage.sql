-- Usage stats. Run this in the Supabase SQL editor after schema.sql and
-- feedback.sql (it uses public.admins / public.is_admin()). Safe to re-run.
--
-- The app counts *active* time (tab visible, input in the last 90 seconds)
-- and files it under the subject and screen the student is on. It sends the
-- totals about once a minute through record_usage(). Admins read everyone's
-- totals with admin_usage_stats() from Profile menu -> User stats.

create table if not exists public.usage_time (
  user_id uuid not null references auth.users(id) on delete cascade,
  day date not null,
  subject text not null check (subject ~ '^[a-z0-9-]{1,40}$'),
  screen text not null check (screen ~ '^[a-z0-9-]{1,40}$'),
  seconds integer not null default 0 check (seconds >= 0 and seconds <= 86400),
  updated_at timestamptz not null default now(),
  primary key (user_id, day, subject, screen)
);

create index if not exists usage_time_day_idx on public.usage_time (day);

alter table public.usage_time enable row level security;

drop policy if exists "Read own or admin usage" on public.usage_time;
create policy "Read own or admin usage"
  on public.usage_time for select
  to authenticated
  using ((select auth.uid()) = user_id or (select public.is_admin()));

-- Writes only go through record_usage(), which clamps what a browser can add.
revoke all on public.usage_time from anon, authenticated;
grant select on public.usage_time to authenticated;

-- entries: [{"day":"2026-11-09","subject":"biology","screen":"learn","seconds":55}, ...]
create or replace function public.record_usage(entries jsonb)
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare
  author_id uuid := auth.uid();
  entry jsonb;
  entry_day date;
  entry_seconds integer;
  total integer := 0;
begin
  if author_id is null then
    raise exception 'Sign in to record usage.';
  end if;
  if entries is null or jsonb_typeof(entries) <> 'array' then
    return;
  end if;
  if jsonb_array_length(entries) > 200 then
    raise exception 'Too many usage entries in one call.';
  end if;

  for entry in select value from jsonb_array_elements(entries) loop
    begin
      entry_day := (entry->>'day')::date;
      entry_seconds := floor((entry->>'seconds')::numeric)::integer;
    exception when others then
      continue;
    end;
    -- Unsent time can wait in the browser for a while, but not forever and
    -- never from the future.
    if entry_day is null
      or entry_day > (now() at time zone 'utc')::date + 1
      or entry_day < (now() at time zone 'utc')::date - 30 then
      continue;
    end if;
    if entry_seconds is null or entry_seconds <= 0 then
      continue;
    end if;
    if coalesce(entry->>'subject', '') !~ '^[a-z0-9-]{1,40}$'
      or coalesce(entry->>'screen', '') !~ '^[a-z0-9-]{1,40}$' then
      continue;
    end if;

    entry_seconds := least(entry_seconds, 43200);
    total := total + entry_seconds;
    if total > 86400 then
      exit;
    end if;

    insert into public.usage_time (user_id, day, subject, screen, seconds)
    values (author_id, entry_day, entry->>'subject', entry->>'screen', entry_seconds)
    on conflict (user_id, day, subject, screen) do update
      set seconds = least(public.usage_time.seconds + excluded.seconds, 86400),
          updated_at = now();
  end loop;
end;
$$;

-- One row per student x subject x screen since since_day (null = all time).
-- Students with no recorded time still appear once, with null subject/screen.
create or replace function public.admin_usage_stats(since_day date default null)
returns table (
  user_id uuid,
  username text,
  joined_at timestamptz,
  subject text,
  screen text,
  seconds bigint,
  active_days bigint,
  last_active timestamptz
)
language plpgsql
security definer
set search_path = ''
stable
as $$
#variable_conflict use_column
begin
  if not public.is_admin() then
    raise exception 'Only admins can read usage stats.';
  end if;

  return query
    with recent as (
      select t.user_id, t.day, t.subject, t.screen, t.seconds, t.updated_at
      from public.usage_time t
      where since_day is null or t.day >= since_day
    ),
    per_user as (
      select r.user_id as uid, count(distinct r.day) as days, max(r.updated_at) as last_at
      from recent r
      group by r.user_id
    ),
    per_bucket as (
      select r.user_id as uid, r.subject as subj, r.screen as scr, sum(r.seconds) as secs
      from recent r
      group by r.user_id, r.subject, r.screen
    )
    select
      p.id,
      p.username,
      p.created_at,
      b.subj,
      b.scr,
      coalesce(b.secs, 0)::bigint,
      coalesce(pu.days, 0)::bigint,
      pu.last_at
    from public.profiles p
    left join per_user pu on pu.uid = p.id
    left join per_bucket b on b.uid = p.id;
end;
$$;

revoke all on function public.record_usage(jsonb) from public;
revoke all on function public.admin_usage_stats(date) from public;
grant execute on function public.record_usage(jsonb) to authenticated;
grant execute on function public.admin_usage_stats(date) to authenticated;
