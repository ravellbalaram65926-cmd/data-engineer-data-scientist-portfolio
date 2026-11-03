"""Email the portfolio owner after all project pipelines and checks pass."""

import os
import smtplib
import ssl
from email.message import EmailMessage

RECIPIENT = "ravellabalaram65926@gmail.com"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def build_message(sender: str, repository: str, commit: str, run_url: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = "Portfolio pipelines successful"
    message["From"] = sender
    message["To"] = RECIPIENT
    message.set_content(
        "All eight portfolio pipelines completed successfully, including lint, "
        "compilation, tests, and pipeline execution.\n\n"
        f"Repository: {repository}\n"
        f"Commit: {commit}\n"
        f"Workflow run: {run_url}\n"
    )
    return message


def main() -> None:
    username = os.environ.get("PORTFOLIO_EMAIL_USERNAME", "")
    password = os.environ.get("PORTFOLIO_EMAIL_APP_PASSWORD", "")
    repository = os.environ["GITHUB_REPOSITORY"]
    commit = os.environ["GITHUB_SHA"]
    server_url = os.environ["GITHUB_SERVER_URL"].rstrip("/")
    run_id = os.environ["GITHUB_RUN_ID"]
    run_number = os.environ["GITHUB_RUN_NUMBER"]
    if not username or not password:
        raise RuntimeError(
            "Set PORTFOLIO_EMAIL_USERNAME and PORTFOLIO_EMAIL_APP_PASSWORD "
            "as GitHub Actions secrets."
        )

    message = build_message(
        username,
        repository,
        commit,
        f"{server_url}/{repository}/actions/runs/{run_id}",
    )
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ssl.create_default_context()) as server:
        server.login(username, password)
        server.send_message(message)
    print(f"Success email sent to {RECIPIENT} for workflow run #{run_number}.")


if __name__ == "__main__":
    main()
