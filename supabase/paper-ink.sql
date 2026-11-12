-- Exam paper markup (pen, highlighter, text boxes) saved to the account, one row
-- per paper. Run this once in the Supabase SQL editor after schema.sql. Safe to re-run.
-- The app keeps working from the browser's local copy until this table exists.

create table if not exists public.paper_ink (
  user_id uuid not null references auth.users(id) on delete cascade,
  file text not null check (char_length(file) between 1 and 300),
  data jsonb not null default '{}'::jsonb check (pg_column_size(data) <= 2000000),
  updated_at timestamptz not null default now(),
  primary key (user_id, file)
);

alter table public.paper_ink enable row level security;

drop policy if exists "Read own paper ink" on public.paper_ink;
create policy "Read own paper ink"
  on public.paper_ink for select
  to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "Insert own paper ink" on public.paper_ink;
create policy "Insert own paper ink"
  on public.paper_ink for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists "Update own paper ink" on public.paper_ink;
create policy "Update own paper ink"
  on public.paper_ink for update
  to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

drop policy if exists "Delete own paper ink" on public.paper_ink;
create policy "Delete own paper ink"
  on public.paper_ink for delete
  to authenticated
  using ((select auth.uid()) = user_id);

grant select, insert, update, delete on public.paper_ink to authenticated;
