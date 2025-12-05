# The Invisible Epidemic: How Catalunya’s Prescription Data Reveals a Mental Health Transformation

> Analyses & Visualization of Big Data — University of Barcelona

Agostina Iozzi - AgostinaIozzi
Gerard Argany - GerardArgany
Isaac Martínez - IsaacMaEs
Sergi Gallego - srurug9818
Vanja Marković - markovicvanja

This repository contains the full analytical pipeline and visual outputs for a data-driven investigation of prescription behaviour in Catalunya.
Using one of Europe’s most detailed public pharmacy-billing datasets, we explore how drug consumption varies by age, sex, time, therapeutic class (ATC), and geographical structure, with a particular emphasis on the Nervous System (ATC N) and mental-health–related medications.

Our goal is not only statistical description but narrative insight: identifying life-course transitions, demographic inequalities, temporal shocks (e.g., COVID-19), and regional disparities.

Our presentation is available [here](https://docs.google.com/presentation/d/10Zp_cbN-qxVcuO1jbMmhXrfdSdAfpXPb/edit?usp=sharing&ouid=107530158480054310317&rtpof=true&sd=true).

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

Raw data (>100MB) are not stored in the repo; they live in a [protected shared drive](https://drive.google.com/drive/folders/1oSEh35RooyFF02pfLBpgv01nmVz6dK72?usp=sharing).

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
- [Sanitary regions](https://analisi.transparenciacatalunya.cat/Salut/Regions-sanit-ries/q2jd-tqye/about_data) and [territorial divisions](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Dades-i-productes/Geoinformacio-cartografica/Divisions-administratives)  
- [Municipal population registers](https://www.idescat.cat/pub/?id=pmh&n=13312&lang=en)  
- [Socioeconomic territorial index](https://www.idescat.cat/pub/?id=ist&n=14034&hist=taules%2Fv2%2Fist%2F14034%2F14994%2Fcom%2Fdata%5Etab%3Dd%2Fr%3D1%2C0%2Ft%3D-1c%3B-0d%2C0)
- [COVID-19 incidence data](https://analisi.transparenciacatalunya.cat/Salut/Registre-de-casos-de-COVID-19-a-Catalunya-per-muni/jj6z-iyrp/about_data)

### Data Types

- Aggregated counts (no personal data)  
- Categorical dimensions: ATC codes, age groups, sex, sanitary region (code)  
- Temporal dimensions (provided as ints): year, month
- Numerical measures: number of prescriptions, total cost, public co-pay amount
- Coordinates in GeoJSON Polygon format

### Storage & Versioning

- Large raw extracts stored on [restricted-access shared drive](https://drive.google.com/drive/folders/1oSEh35RooyFF02pfLBpgv01nmVz6dK72?usp=sharing)
- Processed datasets under 100MB stored in `data/`  
- All transformations documented in Jupyter notebooks  
- Git versioning for full reproducibility

### Privacy & Ethics

- No personal data processed
- Data is aggregated at population level and anonymized
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

Pull the latest raw extracts from the protected drive and place them in a local `data_raw/` folder (ignored by Git). Update notebook paths accordingly.

### Notebooks

Use the files under `scripts/` for exploratory work; when an analysis stabilizes, copy the cleaned narrative (and only necessary cells) into `analysis/` (polished narrative).

### Visual assets

Export plots to `plots/` with descriptive filenames so they can be traced back to the source notebook.

## Project Scope & Analytical Themes

Our story examines:

### 1. How drug consumption evolves across age

- Childhood → dominated by anti-infectives and respiratory drugs
- Early adulthood → chronic/lifestyle conditions begin (digestive, hormonal, musculoskeletal)
- Midlife (45–75) → strong rise in nervous-system and cardiovascular medication
- Older adults (75+) → extensive polypharmacy, with cardiovascular + metabolic dominating

### 2. Regional differences

- Per-capita normalization reveals urban–rural contrasts
- Region × Population structure interactions

### 3. Temporal signals

- Sharp increases in mental-health medication after 2020, especially in young adults
- Broad secular growth across most categories
- Regional differences amplify after COVID

### 4. Nervous System (ATC N) deep-dive

- Level-2 and Level-3 breakdowns
- Age signatures of anxiety, depression, chronic pain treatments
- Evolution before/after COVID-19

### 5. Sex differences in Mental Health

- Male excess in
  - ADHD medications (6–19y)
→ likely due to diagnostic bias: boys are diagnosed earlier, girls remain underdiagnosed
  - Antipsychotics in adolescence

- Female excess in
  - Antidepressants (18–65+)
  - Anxiolytics / Sedatives (30–75)

These mirror known epidemiological patterns, but the age resolution reveals life-course timing very clearly.

## Conclusions & Policy Implications

Prescription data reveal structural mental-health inequalities across age, sex, and territory.

Rising mental-health medication use among young adults after COVID-19 is a strong public health signal.

Female–male asymmetries suggest potential underdiagnosis in girls (ADHD) and over-reliance on anxiolytics among women.

The explosion of polypharmacy in older adults emphasizes the need for integrated care and deprescribing programs.

Territorial disparities may motivate region-specific health interventions.

### Future Work

Would benefit from:

- Per-capita rates by municipality
- Linkage to socioeconomic indicators
- Longitudinal regional cohort decomposition
- Machine-learning clustering of drug profiles
- Time-series forecasting of mental-health burden
- More granular data (daily timestamps, diagnostic codes, prescriber type) would enable stronger causal inference, though such data may not be publicly available.

### License

Creative Commons Attribution (CC BY 4.0) for all derived datasets, plots, and documentation.
Original data remain under their respective public open-data licenses.
