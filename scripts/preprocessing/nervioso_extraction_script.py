#!/usr/bin/env python
"""
This script loads the cleaned prescription dataset ("data_clean.csv"),
extracts only the rows where the ATC Level-1 group corresponds to
"SISTEMA NERVIOSO" (all nervous-system related medications),
and saves this filtered subset as a new file ("data_nervioso.csv").
"""

import pandas as pd
from pathlib import Path

# --------- Config ---------
INPUT_FILE = Path("../data/data_clean.csv")
OUTPUT_FILE = Path("../data/data_nervioso.csv")

NERV_CODE = "SISTEMA NERVIOSO"
COL_ATC_L1 = "grup ATC nivell 1"


def main():
    df = pd.read_csv(INPUT_FILE)

    # Filter nervous-system prescriptions
    df_nerv = df[df[COL_ATC_L1] == NERV_CODE].copy()

    df_nerv.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(df_nerv):,} rows → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
