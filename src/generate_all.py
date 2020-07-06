#!/usr/bin/env python

from generate_metadata import generate_metadata
from generate_appdata import generate_appdata
from generate_downloads import generate_downloads

if __name__ == "__main__":
    generate_metadata()
    generate_appdata()
    generate_downloads()
