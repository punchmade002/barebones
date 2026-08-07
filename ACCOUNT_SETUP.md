# Account backend setup

The site now uses Supabase Auth for email/password accounts, email confirmation,
password resets, cross-device study-state sync, and stable user IDs.

## Supabase configuration

The production project is configured:

- project URL: `https://xzncacwvwaxqcwwtpqql.supabase.co`;
- database objects and Row Level Security policies from `supabase/schema.sql`
  have been applied;
- **Site URL** is `https://barebones.ie`;
- the allowed production redirect is `https://barebones.ie/app.html`;
- the browser-safe publishable key is set in `auth-config.js`.

Before public launch, keep email confirmation enabled and configure a custom
SMTP provider. Supabase's built-in mailer is restricted to project-team
addresses and is not a production password-recovery service.

The publishable key is safe to ship to browsers. Never put a secret or
service-role key in this repository.

## Mailing list

Every email used to create an account is copied by the database trigger into
`public.mailing_list`. This includes self-service registrations and secured
legacy accounts. Applying `supabase/schema.sql` also backfills existing Auth
users.

The table has Row Level Security enabled and no browser-access policy. Only the
Supabase service role can export it. To refresh the local root-level
`mailing list` file:

```sh
SUPABASE_URL=https://your-project.supabase.co \
SUPABASE_SERVICE_ROLE_KEY=your-secret-key \
python3 scripts/export_mailing_list.py
```

The export contains one normalized email per line, starts with an `email`
header, is written with owner-only permissions, and is ignored by Git. Never
put the service-role key in `auth-config.js` or commit the exported list.

Serve the repository over HTTP for local testing; browser auth redirects do not
work reliably from a `file://` URL:

```sh
python3 -m http.server 8000
```

For a live local auth test, temporarily add
`http://localhost:8000/app.html` to Supabase's redirect allow list. Remove it
again before production launch.

## Legacy-account migration

Existing browser profiles remain in `bare-bones-app-v4`. On their next visit,
students are shown **Secure your account** and asked for an email and password.
After email confirmation, the matching local profile is linked to the new
Supabase user ID and uploaded to `study_states`. No progress is deleted.

The existing local `gabriel` profile is prioritised in the migration picker.
Immediately before any legacy profile is linked, the app also writes an
independent `bb-legacy-account-backup-v1:<username>` copy of its study data to
the browser. The original profile remains in `bare-bones-app-v4` as well.
`approved_usernames.txt` is retained as the historical cohort manifest, but it
is no longer used as an authentication check.

Because the old system had no email, password, server record, or private claim
secret, ownership can only be inferred from the existing browser profile. Ask
the existing cohort to secure their accounts before announcing open sign-ups.

## Payment verification boundary

`public.entitlements` is already keyed by the same immutable Auth user ID used
by study data. Signed-in browsers may read only their own entitlement and have
no insert/update/delete permission.

When payments are added:

1. Create Checkout Sessions in a server or Supabase Edge Function.
2. Put the Auth user ID in the payment provider's customer metadata.
3. Verify webhook signatures in that trusted server function.
4. Store provider IDs in `private.billing_customers`.
5. Let the verified webhook—not browser code—write `public.entitlements`.

Never decide paid access from redirect query parameters, client-side metadata,
or an unverified webhook.
