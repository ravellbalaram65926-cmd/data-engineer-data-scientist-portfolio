"""Download the project's Kaggle competition data into the git-ignored folder."""

import argparse
import shutil
import subprocess
import zipfile
from pathlib import Path

COMPETITION = "m5-forecasting-accuracy"


def extract_archives(destination: Path) -> None:
    root = destination.resolve()
    for archive in destination.glob("*.zip"):
        with zipfile.ZipFile(archive) as zipped:
            for entry in zipped.infolist():
                target = (destination / entry.filename).resolve()
                if target != root and root not in target.parents:
                    raise ValueError(f"Unsafe archive path in {archive.name}: {entry.filename}")
            zipped.extractall(destination)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--competition", default=COMPETITION, help="Kaggle competition slug")
    parser.add_argument("--output", type=Path, default=Path("data/external"))
    args = parser.parse_args()

    cli = shutil.which("kaggle")
    if cli is None:
        parser.error("Kaggle CLI missing. Install it with: python -m pip install kaggle")

    args.output.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [cli, "competitions", "download", "-c", args.competition, "-p", str(args.output), "--force"],
        check=True,
    )
    extract_archives(args.output)
    print(f"Downloaded competition {args.competition} into {args.output}")


if __name__ == "__main__":
    main()
