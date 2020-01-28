#!/usr/bin/env python
from pathlib import Path

from format_detailed_occ import format_detailed_occ
from format_simple_occ import format_simple_occ

if __name__ == "__main__":
    # format readable output
    pretty = True

    # create output directory
    Path("../out").mkdir(parents=True, exist_ok=True)

    print("Generating metadata files in the ../out directory")
    format_simple_occ(pretty)
    format_detailed_occ(pretty)
