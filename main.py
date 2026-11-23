#!/usr/bin/env python3
"""make.fun entry: Sum up 23 November's world news in one image.
Deterministic, no network: decodes the bundled base64 image
(entry.png.b64, the entry image stored as text so the repo can hold it)
and writes it to the output directory.
"""
import base64
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png.b64")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(SRC, "rb") as f:
        data = base64.b64decode(f.read())
    with open(OUT, "wb") as f:
        f.write(data)
    try:
        os.chmod(OUT, 0o644)
    except OSError:
        pass  # file is already written; never fail the run on chmod

if __name__ == "__main__":
    main()
