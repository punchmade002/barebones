#!/usr/bin/env python3
"""Build the Supabase Auth email templates in supabase/email-templates/.

Every email shares one layout: warm-grey page, off-white card with an ink
outline and a hard "sticker" shadow, the dot-matrix wordmark, a step tracker
built from dots, a chunky orange button and a little pixel bone in the footer.

Email-client rules followed here: tables for layout, inline styles only, no CSS
variables, absolute image URLs, web fonts with safe fallbacks.

Run:  python3 scripts/build_email_templates.py
Then paste each file into Supabase → Authentication → Emails → Templates
(subjects are listed in supabase/email-templates/README.md).
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "supabase" / "email-templates"

ORANGE = "#fa4c06"
ORANGE_DARK = "#c23504"
ORANGE_SOFT = "#fdd0b0"
ORANGE_TINT = "#fff0e6"
PAGE = "#c9c7c2"
CARD = "#f6f4f0"
CARD_2 = "#edebe6"
INK = "#1a1512"
INK_2 = "#57514a"
LINE = "#d6d2ca"
DOT_OFF = "#d9d5cd"

DISPLAY = "'Archivo', 'Helvetica Neue', Helvetica, Arial, sans-serif"
BODY = "'Hanken Grotesk', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Courier New', Courier, monospace"
LOGO = "https://barebones.ie/design_handoff_barebones_landing/assets/logo-wordmark.png"

# Go template: greet by username when Supabase has one in user_metadata.
HELLO = "{{ if .Data.username }}Hey {{ .Data.username }}{{ else }}Hey there{{ end }}"

# 11 x 5 dot-matrix bone, same rounded-square dots as the wordmark.
BONE = [
    "XX.......XX",
    "XXX.....XXX",
    ".XXXXXXXXX.",
    "XXX.....XXX",
    "XX.......XX",
]


def dot(color, size=8, radius=2):
    return (
        f'<td width="{size}" height="{size}" bgcolor="{color}" '
        f'style="width:{size}px;height:{size}px;background:{color};'
        f'border-radius:{radius}px;font-size:0;line-height:0;">&nbsp;</td>'
    )


def gap(size=2):
    return f'<td width="{size}" style="width:{size}px;font-size:0;line-height:0;">&nbsp;</td>'


def bone(color=ORANGE, size=6):
    rows = []
    for i, row in enumerate(BONE):
        cells = gap(2).join(dot(color if c == "X" else "transparent", size, 2) for c in row)
        rows.append(f"<tr>{cells}</tr>")
        if i < len(BONE) - 1:
            rows.append(f'<tr><td colspan="{len(row) * 2 - 1}" height="2" style="height:2px;font-size:0;line-height:0;">&nbsp;</td></tr>')
    return (
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
        'align="center" style="margin:0 auto;">' + "".join(rows) + "</table>"
    )


def steps(items):
    """items: list of (label, state) where state is done / now / next."""
    cols = []
    for label, state in items:
        if state == "done":
            block, text, mark = ORANGE, INK_2, "&#10003;&nbsp;"
        elif state == "now":
            block, text, mark = ORANGE, ORANGE_DARK, ""
        else:
            block, text, mark = DOT_OFF, INK_2, ""
        # Each step is a 4-dot bar; the current step's last dot is hollow
        # (half-done) so it reads like a loading bar caught mid-way.
        dots = []
        for i in range(4):
            colour = block
            if state == "now" and i == 3:
                colour = ORANGE_SOFT
            dots.append(dot(colour, 12, 3))
        bar = gap(3).join(dots)
        weight = "800" if state == "now" else "600"
        cols.append(
            f'<td align="left" valign="top" style="padding:0 10px 0 0;">'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>{bar}</tr></table>'
            f'<div style="font-family:{BODY};font-size:12px;line-height:16px;font-weight:{weight};'
            f'color:{text};padding-top:7px;white-space:nowrap;">{mark}{label}</div></td>'
        )
    return (
        '<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 26px;">'
        f'<tr>{"".join(cols)}</tr></table>'
    )


def button(href, label):
    return f"""
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:6px 0 8px;">
  <tr>
    <td bgcolor="{ORANGE}" style="background:{ORANGE};border:2px solid {INK};border-radius:14px;box-shadow:4px 4px 0 {INK};">
      <a href="{href}" target="_blank"
         style="display:inline-block;padding:15px 26px;font-family:{DISPLAY};font-size:17px;line-height:20px;
                font-weight:800;color:#ffffff;text-decoration:none;letter-spacing:0.01em;border-radius:12px;">
        {label}&nbsp;&rarr;
      </a>
    </td>
  </tr>
</table>"""


def fallback_link(href):
    return f"""
<p style="margin:22px 0 0;font-family:{BODY};font-size:13px;line-height:19px;color:{INK_2};">
  Button not working? Paste this into your browser:
</p>
<p style="margin:6px 0 0;padding:10px 12px;background:{CARD_2};border-radius:10px;
          font-family:{MONO};font-size:12px;line-height:17px;color:{INK};word-break:break-all;">
  <a href="{href}" target="_blank" style="color:{ORANGE_DARK};text-decoration:underline;">{href}</a>
</p>"""


def code_box(token):
    return f"""
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:4px 0 8px;">
  <tr>
    <td bgcolor="{ORANGE_TINT}" style="background:{ORANGE_TINT};border:2px dashed {ORANGE};border-radius:14px;padding:16px 26px;">
      <span style="font-family:{MONO};font-size:34px;line-height:38px;font-weight:700;letter-spacing:0.28em;color:{INK};">{token}</span>
    </td>
  </tr>
</table>"""


def layout(*, title, preheader, kicker, headline, body_html, action_html, note):
    return f"""<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="color-scheme" content="light only" />
<meta name="supported-color-schemes" content="light only" />
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&amp;family=Hanken+Grotesk:wght@400;600;700&amp;display=swap" rel="stylesheet" />
<style>
  @media (max-width: 520px) {{
    .bb-card {{ padding: 30px 22px 28px !important; }}
    .bb-headline {{ font-size: 30px !important; line-height: 33px !important; }}
  }}
  a {{ color: {ORANGE_DARK}; }}
</style>
</head>
<body style="margin:0;padding:0;background:{PAGE};-webkit-text-size-adjust:100%;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">{preheader}&#8202;&#847;&#8202;&#847;&#8202;&#847;&#8202;&#847;&#8202;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{PAGE}" style="background:{PAGE};">
  <tr>
    <td align="center" style="padding:36px 14px 40px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:560px;">
        <tr>
          <td align="left" style="padding:0 6px 18px;">
            <a href="https://barebones.ie" target="_blank" style="text-decoration:none;">
              <img src="{LOGO}" width="168" alt="barebones" style="display:block;width:168px;height:auto;border:0;" />
            </a>
          </td>
        </tr>
        <tr>
          <td class="bb-card" bgcolor="{CARD}"
              style="background:{CARD};border:2px solid {INK};border-radius:22px;box-shadow:8px 8px 0 {INK};padding:38px 38px 34px;">
            <div style="font-family:{DISPLAY};font-size:12px;line-height:14px;font-weight:800;letter-spacing:0.16em;
                        text-transform:uppercase;color:{ORANGE};margin:0 0 12px;">
              <span style="display:inline-block;width:8px;height:8px;background:{ORANGE};border-radius:2px;margin-right:7px;vertical-align:1px;"></span>{kicker}
            </div>
            <h1 class="bb-headline" style="margin:0 0 18px;font-family:{DISPLAY};font-size:36px;line-height:38px;font-weight:900;
                       letter-spacing:-0.025em;color:{INK};">{headline}</h1>
            {body_html}
            {action_html}
          </td>
        </tr>
        <tr>
          <td style="padding:22px 10px 0;">
            <p style="margin:0;font-family:{BODY};font-size:13px;line-height:19px;color:{INK_2};text-align:center;">{note}</p>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding:26px 0 8px;">{bone()}</td>
        </tr>
        <tr>
          <td align="center" style="padding:6px 0 0;">
            <p style="margin:0;font-family:{DISPLAY};font-size:12px;line-height:16px;font-weight:700;letter-spacing:0.08em;color:{INK};">
              BAREBONES &middot; LEAVING CERT, DOWN TO THE BONES
            </p>
            <p style="margin:6px 0 0;font-family:{BODY};font-size:12px;line-height:16px;color:{INK_2};">
              <a href="https://barebones.ie" target="_blank" style="color:{INK_2};text-decoration:underline;">barebones.ie</a>
              &nbsp;&middot;&nbsp;
              <a href="https://barebones.ie/privacy.html" target="_blank" style="color:{INK_2};text-decoration:underline;">Privacy</a>
            </p>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</body>
</html>
"""


def para(text, margin="0 0 22px"):
    return f'<p style="margin:{margin};font-family:{BODY};font-size:16px;line-height:25px;color:{INK};">{text}</p>'


def highlight(text):
    return (
        f'<span style="background:{ORANGE_TINT};border-radius:6px;padding:1px 6px;'
        f'font-weight:700;color:{INK};">{text}</span>'
    )


URL = "{{ .ConfirmationURL }}"

TEMPLATES = {
    "confirm-signup.html": dict(
        subject="Confirm your email, one click and you're in",
        title="Confirm your barebones account",
        preheader="One click to finish setting up your account. Your flashcards are waiting.",
        kicker="One last thing",
        headline=f'{HELLO}, you&rsquo;re nearly in<span style="color:{ORANGE};">.</span>',
        body_html=steps([("Sign up", "done"), ("Confirm email", "now"), ("Start studying", "next")])
        + para(
            "Tap the button to confirm this is your email. Then your account is ready: "
            "flashcards, past-paper questions and your progress, saved on every device."
        ),
        action_html=button(URL, "Confirm my email") + fallback_link(URL),
        note="Didn&rsquo;t sign up for barebones? Ignore this email. Nothing happens without the click.",
    ),
    "reset-password.html": dict(
        subject="Reset your barebones password",
        title="Reset your barebones password",
        preheader="Choose a new password. Your progress is safe either way.",
        kicker="Locked out? It happens",
        headline=f'Let&rsquo;s get you a new password<span style="color:{ORANGE};">.</span>',
        body_html=para(
            f"Someone (hopefully you) asked to reset the password for {highlight('{{ .Email }}')}. "
            "Tap below to choose a new one. Your study progress stays exactly where it is."
        ),
        action_html=button(URL, "Choose a new password") + fallback_link(URL),
        note="Didn&rsquo;t ask for this? Ignore it and your password stays the same.",
    ),
    "magic-link.html": dict(
        subject="Your barebones sign-in link",
        title="Sign in to barebones",
        preheader="Your one-tap sign-in link is inside.",
        kicker="Knock knock",
        headline=f'Your sign-in link is here<span style="color:{ORANGE};">.</span>',
        body_html=para(
            f"{HELLO}. Tap below to sign straight in to barebones. No password needed, "
            "and the link only works once."
        ),
        action_html=button(URL, "Sign me in") + fallback_link(URL),
        note="Didn&rsquo;t try to sign in? Ignore this email and nobody gets in.",
    ),
    "change-email.html": dict(
        subject="Confirm your new email for barebones",
        title="Confirm your new email",
        preheader="Confirm the switch to your new inbox.",
        kicker="New inbox, who dis?",
        headline=f'Moving to a new inbox<span style="color:{ORANGE};">?</span>',
        body_html=steps([("Old email", "done"), ("Confirm switch", "now"), ("All set", "next")])
        + para(
            f"You asked to change your barebones email from {highlight('{{ .Email }}')} "
            f"to {highlight('{{ .NewEmail }}')}. Confirm it and we&rsquo;ll send everything there from now on."
        ),
        action_html=button(URL, "Confirm new email") + fallback_link(URL),
        note="Didn&rsquo;t ask for this? Ignore it and your email stays the same.",
    ),
    "invite-user.html": dict(
        subject="You're invited to barebones",
        title="You're invited to barebones",
        preheader="Someone saved you a seat. Accept to start studying.",
        kicker="You&rsquo;ve got an invite",
        headline=f'Someone saved you a seat<span style="color:{ORANGE};">.</span>',
        body_html=para(
            "You&rsquo;ve been invited to barebones, Leaving Cert study stripped down to what "
            "actually comes up. Accept below to set up your account."
        ),
        action_html=button(URL, "Accept invite") + fallback_link(URL),
        note="Not expecting this? You can ignore it safely.",
    ),
    "reauthentication.html": dict(
        subject="Your barebones confirmation code",
        title="Your barebones confirmation code",
        preheader="Here's the code you asked for.",
        kicker="Quick security check",
        headline=f'Here&rsquo;s your code<span style="color:{ORANGE};">.</span>',
        body_html=para("Type this into barebones to confirm it&rsquo;s really you:", "0 0 14px"),
        action_html=code_box("{{ .Token }}")
        + para("It expires soon, so use it now.", "14px 0 0"),
        note="Didn&rsquo;t ask for a code? Ignore this email. Someone may have typed your address by mistake.",
    ),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    readme = [
        "# Supabase email templates",
        "",
        "Generated by `scripts/build_email_templates.py`; edit the script, not these files.",
        "",
        "Paste each file into **Supabase → Authentication → Emails → Templates**, using",
        "the matching template and subject below. The `{{ ... }}` parts are Supabase",
        "template variables and must stay as they are.",
        "",
        "| Supabase template | File | Subject |",
        "|---|---|---|",
    ]
    names = {
        "confirm-signup.html": "Confirm signup",
        "invite-user.html": "Invite user",
        "magic-link.html": "Magic link",
        "change-email.html": "Change email address",
        "reset-password.html": "Reset password",
        "reauthentication.html": "Reauthentication",
    }
    for filename, spec in TEMPLATES.items():
        spec = dict(spec)
        subject = spec.pop("subject")
        (OUT / filename).write_text(layout(**spec), encoding="utf-8")
        readme.append(f"| {names[filename]} | `{filename}` | {subject} |")
    (OUT / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    print(f"Wrote {len(TEMPLATES)} templates to {OUT}")


if __name__ == "__main__":
    main()
