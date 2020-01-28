#!/usr/bin/env python
from pathlib import Path

from format_simple_occ import format_simple_occ
from format_detailed_occ import format_detailed_occ
from format_default import format_default
from format_cohort_years import format_cohort_years

if __name__ == "__main__":
    # set year range for cohort labels
    start_year = 2000
    end_year = 2015

    # format readable output [pretty/minify/other]
    json_format = 'minify'

    # create output directory
    Path("../out").mkdir(parents=True, exist_ok=True)

    # handling for custom logic of occ/mos labels
    print("Generating metadata files in the ../out directory")
    format_simple_occ(json_format)
    format_detailed_occ(json_format)

    # handling for default layout
    format_default("label_afqtgrp", "afqtgrp", json_format)
    format_default("label_agegrp", "agegrp", json_format)
    format_default("label_education", "education", json_format)
    format_default("label_ethnicity", "ethnicity", json_format)
    format_default("label_fipsnum", "geography", json_format)
    format_default("label_industry", "industry", json_format)
    format_default("label_paygrade", "paygrade", json_format)
    format_default("label_race", "race", json_format)
    format_default("label_sex", "sex", json_format)
    format_default("label_yosgrp", "yosgrp", json_format)

    # add custom year labels per cohort size
    format_cohort_years(start_year, end_year, 2, json_format)
    format_cohort_years(start_year, end_year, 4, json_format)
    format_cohort_years(start_year, end_year, 8, json_format)
