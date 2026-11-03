import unittest
from email.message import EmailMessage
from unittest.mock import patch

from scripts.send_success_email import (
    RECIPIENT,
    build_message,
    main,
    send_success_email,
)


class SuccessEmailTests(unittest.TestCase):
    def test_builds_message_with_run_details(self):
        message = build_message(
            "sender@example.com",
            "owner/repository",
            "abc123",
            "https://github.com/owner/repository/actions/runs/10",
        )
        self.assertIsInstance(message, EmailMessage)
        self.assertEqual(message["To"], RECIPIENT)
        self.assertIn("all eight portfolio pipelines", message.get_content().lower())
        self.assertIn("abc123", message.get_content())
        self.assertIn("/runs/10", message.get_content())

    @patch("scripts.send_success_email.smtplib.SMTP_SSL")
    def test_sends_using_gmail_smtp(self, smtp_ssl):
        server = smtp_ssl.return_value.__enter__.return_value
        send_success_email(
            "sender@example.com",
            "app-password",
            "owner/repository",
            "abc123",
            "https://github.com/owner/repository/actions/runs/10",
        )
        server.login.assert_called_once_with("sender@example.com", "app-password")
        sent = server.send_message.call_args.args[0]
        self.assertEqual(sent["To"], RECIPIENT)
        self.assertIn("abc123", sent.get_content())

    @patch.dict(
        "os.environ",
        {
            "GITHUB_REPOSITORY": "owner/repository",
            "GITHUB_SHA": "abc123",
            "GITHUB_SERVER_URL": "https://github.com",
            "GITHUB_RUN_ID": "10",
            "GITHUB_RUN_NUMBER": "2",
        },
        clear=True,
    )
    def test_requires_credentials(self):
        with self.assertRaisesRegex(RuntimeError, "PORTFOLIO_EMAIL_USERNAME"):
            main()


if __name__ == "__main__":
    unittest.main()
