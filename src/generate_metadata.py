#!/usr/bin/env python

from format_simple_occ import format_simple_occ
from format_detailed_occ import format_detailed_occ

if __name__ == "__main__":
    pretty = True
    print("Generating metadata files in the ../out directory")
    format_simple_occ(pretty)
    #format_detailed_occ(pretty)
