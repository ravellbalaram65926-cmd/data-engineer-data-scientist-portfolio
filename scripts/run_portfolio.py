"""Run every project demo pipeline and/or its focused tests."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = (
    "retail-demand-forecasting",
    "real-time-fraud-detection",
    "end-to-end-mlops-platform",
    "customer-analytics-warehouse",
    "rag-document-search-pipeline",
    "recommendation-engine-at-scale",
    "iot-energy-demand-forecasting",
    "data-quality-and-anomaly-monitoring",
)


def run(command: list[str], cwd: Path) -> None:
    print(f"\n==> {cwd.name}: {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--pipelines-only", action="store_true")
    mode.add_argument("--tests-only", action="store_true")
    parser.add_argument(
        "--email-on-success",
        action="store_true",
        help="Send the success email after all selected projects pass.",
    )
    args = parser.parse_args()
    for name in PROJECTS:
        project = ROOT / name
        if not args.tests_only:
            run([sys.executable, "src/main.py"], project)
        if not args.pipelines_only:
            run([sys.executable, "-m", "pytest", "-q", "tests"], project)
    if args.email_on_success:
        environment = os.environ.copy()
        environment.setdefault(
            "GITHUB_REPOSITORY",
            "ravellbalaram65926-cmd/data-engineer-data-scientist-portfolio",
        )
        environment.setdefault("GITHUB_SHA", "local run")
        environment.setdefault("GITHUB_SERVER_URL", "https://github.com")
        environment.setdefault("GITHUB_RUN_ID", "local")
        environment.setdefault("GITHUB_RUN_NUMBER", "local")
        email_command = [
            sys.executable,
            str(ROOT / "scripts" / "send_success_email.py"),
        ]
        print(f"\n==> Sending success email: {' '.join(email_command)}", flush=True)
        subprocess.run(
            email_command,
            cwd=ROOT,
            env=environment,
            check=True,
        )


if __name__ == "__main__":
    main()
