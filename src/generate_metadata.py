#!/usr/bin/env python
from pathlib import Path

from format_default import format_default
from format_detailed_occ import format_detailed_occ
from format_simple_occ import format_simple_occ

if __name__ == "__main__":
    # format readable output
    pretty = True

    # create output directory
    Path("../out").mkdir(parents=True, exist_ok=True)

    # handling for custom logic of occ/mos labels
    print("Generating metadata files in the ../out directory")
    format_simple_occ(pretty)
    format_detailed_occ(pretty)

    # handling for default layout
    format_default("label_afqtgrp", "afqtgrp", pretty)
