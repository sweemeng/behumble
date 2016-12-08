import re

ms_pattern = re.compile("^[Mm]s\.?\W+?")
miss_pattern = re.compile("^[Mm]iss\.?\W+?")
mr_pattern = re.compile("^[Mm]r\.?\W+?")
mrs_pattern = re.compile("^[Mm]rs\.?\W+?")
dr_pattern = re.compile("^[Dd]r\.?\W+?")

patterns = (
        ms_pattern,
        mr_pattern,
        mrs_pattern,
        dr_pattern,
        miss_pattern,
        )
