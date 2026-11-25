"""Write the shipped excuse line to the grader output directory.

Reads entry.txt next to this script and copies it byte for byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
Standard library only, no network, deterministic output.

The write is direct: no temporary file and no rename, so the output
keeps the explicit 0644 mode the grader needs to read it.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    data = (HERE / "entry.txt").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_bytes(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        raise SystemExit(f"cannot write output entry: {exc}") from exc


if __name__ == "__main__":
    main()
