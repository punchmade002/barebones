#!/usr/bin/env python3
"""Export the protected Supabase mailing list to the repository root."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def required_environment(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} is required")
    return value


def fetch_emails(supabase_url: str, service_role_key: str) -> list[str]:
    query = urlencode(
        {
            "select": "email",
            "order": "created_at.asc",
        }
    )
    request = Request(
        f"{supabase_url.rstrip('/')}/rest/v1/mailing_list?{query}",
        headers={
            "apikey": service_role_key,
            "Authorization": f"Bearer {service_role_key}",
            "Accept": "application/json",
        },
    )

    with urlopen(request, timeout=30) as response:
        rows = json.load(response)

    return sorted(
        {
            str(row.get("email", "")).strip().lower()
            for row in rows
            if str(row.get("email", "")).strip()
        }
    )


def write_export(output_path: Path, emails: list[str]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, temporary_name = tempfile.mkstemp(
        dir=output_path.parent,
        prefix=".mailing-list-",
        text=True,
    )
    temporary_path = Path(temporary_name)

    try:
        with os.fdopen(file_descriptor, "w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream, lineterminator="\n")
            writer.writerow(["email"])
            writer.writerows([email] for email in emails)
        os.chmod(temporary_path, stat.S_IRUSR | stat.S_IWUSR)
        temporary_path.replace(output_path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise


def main() -> int:
    repository_root = Path(__file__).resolve().parent.parent
    output_path = repository_root / "mailing list"

    try:
        supabase_url = required_environment("SUPABASE_URL")
        service_role_key = required_environment("SUPABASE_SERVICE_ROLE_KEY")
        emails = fetch_emails(supabase_url, service_role_key)
        write_export(output_path, emails)
    except (RuntimeError, HTTPError, URLError, json.JSONDecodeError) as error:
        print(f"Could not export mailing list: {error}", file=sys.stderr)
        return 1

    print(f"Exported {len(emails)} email(s) to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
