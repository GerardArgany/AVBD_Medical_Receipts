# Catalunya Prescriptions Data Story

> Analyses & Visualization of Big Data — University of Barcelona

This project develops a comprehensive, data-driven narrative about prescription behaviors in Catalunya using anonymized public reimbursement data from CatSalut.
Our analysis investigates how drug consumption patterns vary across age, time, therapeutic class (ATC hierarchy), geography, and population characteristics, with a particular emphasis on nervous-system (ATC N) and mental-health–related prescriptions.

The goal is not only statistical exploration but storytelling: identifying transitions in life stages, signals of chronicity, demographic inequalities, and temporal anomalies (COVID, seasonal patterns, regional disparities).

## Repository Overview

```
.
├── analysis/                           # Clean, narrative-ready notebooks
├── scripts/                            # Experimental sandbox notebooks
│   └── preprocessing/                  # Preprocessing/cleaning scripts
├── plots/                              # All exported visual assets
├── data/                               # Small or intermediate CSVs (<100MB)
├── requirements.txt
├── LICENSE
└── README.md

```

## Introduction

Understanding how medications are prescribed across a population offers a unique window into the health needs, inequalities, and long-term trends of that society. Catalunya maintains one of the most complete and publicly accessible pharmaceutical billing datasets in Europe, making it an ideal case study for data-driven public health storytelling.

This project uses the [*Receptes facturades al Servei Català de la Salut*](https://datos.gob.es/es/catalogo/a09002970-recetas-facturadas-al-servei-catala-de-la-salut) dataset — a monthly, aggregated record of all reimbursed outpatient prescriptions — to explore:

- how medication consumption changes with age,
- how patterns vary across regions, sexes, and population structures,
- how major events (e.g., COVID-19) affected mental-health–related prescriptions,
- and how therapeutic categories evolve across the life course.

Our central theme is the Nervous System (ATC N) group, which includes psycholeptics, psychoanaleptics, anxiolytics, antipsychotics, antidepressants and other mental-health–related medicines.  
We combine this with regional population data and demographic signals to build an evidence-based data story about the rise, evolution, and demographic structure of mental-health drug use in Catalunya.

## What is the ATC Classification System?

The ATC (Anatomical Therapeutic Chemical) classification is an international system used to group and code medicines.  
Each drug is assigned codes that reflect:

- **Level 1 – Organ system** (e.g., N = Nervous System, C = Cardiovascular System)  
- **Level 2 – Therapeutic main group** (e.g., antidepressants, antipsychotics)  
- **Level 3 – Pharmacological subgroup**  
- **Level 4 – Chemical subgroup**

This hierarchical structure allows us to zoom from a high-level overview (e.g., which organ systems dominate?) down to fine-grained mechanisms (e.g., which subclasses of antidepressants grow fastest in ages 45–60).

## Project Motivation

Mental-health drug use has been steadily increasing worldwide, particularly in Europe. In Catalunya, the Nervous System group (ATC N):

- grows faster than most other therapeutic systems,
- peaks in working-age and early-senior adults,
- shows strong gender differences,
- varies substantially across regions,
- and presents clear temporal signatures around major events such as COVID-19.

These trends are not immediately visible without combining age, time, and geography.  
This project aims to make them visible, interpretable, and narratively coherent using modern data visualization and exploratory analytics.

## Data Management Summary

### Data Sources

We use public, aggregated, anonymized datasets released by:

- Dades Obertes de Catalunya (Generalitat de Catalunya)  
- Idescat (Statistical Institute of Catalonia)  
- Institut Cartogràfic i Geològic de Catalunya (ICGC)

Key datasets include:

- [Receptes facturades al Servei Català de la Salut]((https://datos.gob.es/es/catalogo/a09002970-recetas-facturadas-al-servei-catala-de-la-salut)) (prescriptions, 2016–2025)  
- Sanitary regions and territorial divisions  
- Municipal population registers  
- Socioeconomic territorial index  
- COVID-19 incidence data

### Data Types

- Aggregated counts (no personal data)  
- Categorical dimensions: ATC codes, age groups, sex, sanitary region  
- Temporal dimensions (provided as ints): year, month
- Numerical measures: number of prescriptions/envases, total cost, public co-pay amount

### Storage & Versioning

- Large raw extracts stored on [restricted-access shared drive](https://drive.google.com/drive/folders/1oSEh35RooyFF02pfLBpgv01nmVz6dK72?usp=sharing)
- Processed datasets under 100MB stored in `data/`  
- All transformations documented in Jupyter notebooks  
- Scripts tracked via Git for full reproducibility

### Privacy & Ethics

- No personal data processed  
- Fully GDPR compliant  
- All datasets licensed for reuse with attribution  

### Preservation

- Raw data preserved on shared drive  
- Analysis scripts preserved in repository for long-term reproducibility  
- All plots and tables are reproducible from source notebooks

## Working With The Project

### 1. Environment Setup

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Data Access

Place raw extracts inside a local `data_raw/` (make sure to ignore it by Git).
Use `data/` only for small, processed, anonymized CSVs.

ull the latest raw extracts from the protected drive and place them in a local `data_raw/` folder (ignored by Git). Update notebook paths accordingly.

### Notebooks

Use the files under `scripts/` for exploratory work; when an analysis stabilizes, copy the cleaned narrative (and only necessary cells) into `analysis/` (polished narrative).

### Visual assets

Export plots to `plots/` with descriptive filenames so they can be traced back to the source notebook.

## Project Scope & Analytical Themes

Our story examines:

### 1. How drug consumption evolves across age

- childhood = anti-infectives & respiratory
- adulthood = chronic metabolic & cardiovascular
- 45–70 = nervous-system dominance emerges
- 75+ = strong multi-morbidity

### 2. Regional differences

- Per-capita normalization reveals urban–rural contrasts
- Detection of outlier regions (e.g., Terres de l’Ebre anomalies)

### 3. Temporal signals

- COVID-19 shifts
- Seasonality across therapeutic classes
- Long-term secular trends (2016–2025)

### 4. Nervous System (ATC N) deep-dive

- Level-3 and Level-4 breakdowns
- Age signatures of anxiety, depression, chronic pain treatments
- Evolution before/after COVID-19

### 5. Demographic inequalities

- Age × Sex patterns
- Region × Population structure interactions
