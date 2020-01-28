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
    format_default("label_agegrp", "agegrp", pretty)
    format_default("label_education", "education", pretty)
    format_default("label_ethnicity", "ethnicity", pretty)
    format_default("label_fipsnum", "geography", pretty)
    format_default("label_industry", "industry", pretty)
    format_default("label_paygrade", "paygrade", pretty)
    format_default("label_race", "race", pretty)
    format_default("label_sex", "sex", pretty)
    format_default("label_yosgrp", "yosgrp", pretty)

    # add custom year labels per cohort size
    format_cohort_years(start_year, end_year, 2, pretty)
    format_cohort_years(start_year, end_year, 4, pretty)
    format_cohort_years(start_year, end_year, 8, pretty)
