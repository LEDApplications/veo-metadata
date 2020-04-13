#!/usr/bin/env python

from utils import create_zip

if __name__ == "__main__":
    # TODO add state and state x occ data back into exports
    print("Generating zip files...")

    # to get the components that go into a zip file, go into the views directory of the frontend and run
    # $ grep -r ":url" .
    # creat the zipfile by using the create_zip util

    # ./ occupation / Paygrade.vue: < GetData: url = "dataPath('metadata/label_dod_occ_code.json')" >
    # ./ occupation / Paygrade.vue: < GetData: url = "dataPath('metadata/label_paygrade_groups.json')" >
    # ./ occupation / Paygrade.vue: < GetData: url = "dataPath('metadata/label_4year_cohorts.json')" >
    # ./ occupation / Paygrade.vue::url = "dataPath('data/veoo2p.csv')"
    create_zip("../out/OccupationByPaygrade.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_dod_occ_code.csv",
               "../raw/label_paygrade.csv",
               "../raw/label_paygrade_level.csv",
               "../raw/veoo2p.csv")

    # ./ occupation / Detail.vue: < GetData: url = "dataPath('metadata/label_dod_occ_code_detailed.json')" >
    # ./ occupation / Detail.vue: < GetData: url = "dataPath('metadata/label_8year_cohorts.json')" >
    # ./ occupation / Detail.vue::url = "dataPath('data/veoo3.csv')"
    create_zip("../out/DetailedOccupation.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_dod_occ_code.csv",
               "../raw/label_dod_occ_code_w_mosc.csv",
               "../raw/veoo3.csv")

    # ./ occupation / Industry.vue: < GetData: url = "dataPath('metadata/label_dod_occ_code.json')" >
    # ./ occupation / Industry.vue: < GetData: url = "dataPath('metadata/label_industry.json')" >
    # ./ occupation / Industry.vue: < GetData: url = "dataPath('metadata/label_4year_cohorts.json')" >
    # ./ occupation / Industry.vue::url = "dataPath('data/veoo2ns.csv')"
    create_zip("../out/OccupationByIndustry.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_dod_occ_code.csv",
               "../raw/label_industry.csv",
               "../raw/label_ind_level.csv",
               "../raw/veoo2ns.csv")

    # ./ time / Paygrade.vue: < GetData: url = "dataPath('metadata/label_paygrade.json')" >
    # ./ time / Paygrade.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / Paygrade.vue::url = "dataPath('data/veop.csv')"
    create_zip("../out/Paygrade.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_paygrade.csv",
               "../raw/label_paygrade_level.csv",
               "../raw/veop.csv")

    # ./ time / RaceEthnicity.vue: < GetData: url = "dataPath('metadata/label_race.json')" >
    # ./ time / RaceEthnicity.vue: < GetData: url = "dataPath('metadata/label_ethnicity.json')" >
    # ./ time / RaceEthnicity.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / RaceEthnicity.vue::url = "dataPath('data/veorh.csv')"
    create_zip("../out/RaceEthnicity.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_race.csv",
               "../raw/label_ethnicity.csv",
               "../raw/veorh.csv")

    # ./ time / AFQT.vue: < GetData: url = "dataPath('metadata/label_afqtgrp.json')" >
    # ./ time / AFQT.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / AFQT.vue::url = "dataPath('data/veot.csv')"
    create_zip("../out/AFQT.zip", "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_afqtgrp.csv",
               "../raw/veot.csv")

    # ./ time / Age.vue: < GetData: url = "dataPath('metadata/label_agegrp.json')" >
    # ./ time / Age.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / Age.vue::url = "dataPath('data/veoa.csv')"
    create_zip("../out/Age.zip", "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_agegrp.csv",
               "../raw/veoa.csv")

    # ./ time / YearsOfService.vue: < GetData: url = "dataPath('metadata/label_yosgrp.json')" >
    # ./ time / YearsOfService.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / YearsOfService.vue::url = "dataPath('data/veox.csv')"
    create_zip("../out/YearsOfService.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_yosgrp.csv",
               "../raw/veox.csv")

    # ./ time / Industry.vue: < GetData: url = "dataPath('metadata/label_industry.json')" >
    # ./ time / Industry.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / Industry.vue::url = "dataPath('data/veons.csv')"
    create_zip("../out/Industry.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_industry.csv",
               "../raw/label_ind_level.csv",
               "../raw/veons.csv")

    # ./ time / Sex.vue: < GetData: url = "dataPath('metadata/label_sex.json')" >
    # ./ time / Sex.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / Sex.vue::url = "dataPath('data/veos.csv')"
    create_zip("../out/Sex.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_sex.csv",
               "../raw/veos.csv")

    # ./ time / Education.vue: < GetData: url = "dataPath('metadata/label_education.json')" >
    # ./ time / Education.vue: < GetData: url = "dataPath('metadata/label_2year_cohorts.json')" >
    # ./ time / Education.vue::url = "dataPath('data/veoe.csv')"
    create_zip("../out/Education.zip",
               "../raw/release_schema.csv",
               "../raw/tablelist.csv",
               "../raw/label_cohort.csv",
               "../raw/label_cohort_years.csv",
               "../raw/label_education.csv",
               "../raw/veoe.csv")

    print("Done.")
