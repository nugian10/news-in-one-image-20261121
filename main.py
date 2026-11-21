#!/usr/bin/env python3
"""make.fun news-image-20261121 entry.

Copies the committed front-page image (entry.png, beside this file) to
$MAKEFUN_OUTPUT_DIR/entry.png (the grader's /output). Standard library only.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"

# sha256 of the committed front page; the copy is verified against it so a
# truncated or swapped image can never be submitted silently.
EXPECTED_SHA256 = "7b591760595308ba57e95f6982f0c4a874c43e7ee5c0d037399a82c8292f5955"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if sha256_of(SOURCE) != EXPECTED_SHA256:
        raise SystemExit("entry.png does not match its recorded sha256")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    if sha256_of(target) != EXPECTED_SHA256:
        raise SystemExit("copied entry.png does not match its recorded sha256")


if __name__ == "__main__":
    main()
