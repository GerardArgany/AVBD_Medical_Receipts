"""
Script to:
1. Load a CSV dataset.
2. Normalize age group labels (merge equivalent categories).
3. Aggregate metrics over the new age groups.
4. Save the cleaned dataset.
"""

import re
from pathlib import Path

import pandas as pd

# --------- Config ---------
CSV_PATH = Path("../data/data_original.csv")
OUT_FILE = Path("../data/data_clean.csv")

AGE_COL = "grup d'edat"

GROUP_COLS = [
    "any",
    "mes",
    "codi de la regió sanitària",
    "regió sanitària",
    "grup d'edat",
    "sexe",
    "codi del grup ATC nivell 1",
    "grup ATC nivell 1",
    "codi del grup ATC nivell 2",
    "grup ATC nivell 2",
    "codi del grup ATC nivell 3",
    "grup ATC nivell 3",
    "codi del grup ATC nivell 4",
    "grup ATC nivell 4",
]

AGG_COLS = {
    "nombre de receptes": "sum",
    "nombre d'envasos": "sum",
    "import íntegre": "sum",
    "import aportació CatSalut": "sum",
}

# Precompile regex for age ranges like "60-64" or "60-64 anys"
AGE_RANGE_RE = re.compile(r"(\d{1,2})-(\d{1,2})")


def clean_age_label(label: str) -> str:
    """
    Normalize age group labels.

    Examples:
        "Més de 84 anys" -> "85+"
        "20-24 anys"     -> "20-24"
        "Altres"         -> "Altres" (unchanged)
    """
    if not isinstance(label, str):
        return label

    x = label.strip()

    if x in {"Altres", "Sense especificar"}:
        return x

    # "Més de 84 anys" or "Més de 84"
    if x.startswith("Més de"):
        return "85+"

    # "60-64", "60-64 anys", etc.
    match = AGE_RANGE_RE.match(x)
    if match:
        lo, hi = match.groups()
        return f"{lo}-{hi}"

    return x


def main() -> None:
    # Load
    df = pd.read_csv(CSV_PATH)

    # Clean age labels
    df = df.rename(columns={AGE_COL: "age_raw"})
    df["grup d'edat"] = df["age_raw"].apply(clean_age_label)
    df = df.drop(columns=["age_raw"])

    # Aggregate over normalized age groups
    df_clean = df.groupby(GROUP_COLS, as_index=False).agg(AGG_COLS)

    # Save
    df_clean.to_csv(OUT_FILE, index=False)


if __name__ == "__main__":
    main()
