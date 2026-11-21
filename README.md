# Neonatal mortality with NCHS data

> **Framework.** This repository applies the thesis's staged framework for clinical prediction models. The framework (stages, gates, criteria and literature) and the catalogue of models with their status are in [StagedFramework_ClinicalPrediction](https://github.com/khem777/StagedFramework_ClinicalPrediction).

Can live births at high risk of dying in their first 28 days be identified at birth? This model uses the public-use linked birth/infant death files of the National Center for Health Statistics (NCHS, CDC) and follows the staged framework for clinical prediction models.

> **Status (2026-11-20): data adapter done.** The 8 birth cohorts (2016–2023) are built, with 100% of infant deaths joined to their birth ([`data/outputs_01_build_cohorts.txt`](data/outputs_01_build_cohorts.txt)). Next: count audit.

[Versión en español](README_es.md)

## Scope

- **Outcome:** neonatal death (0 to 27 days of life).
- **Population:** live births to US-resident mothers, 22 weeks of gestation or more, birth cohorts 2016 to 2023 (about 3.6 to 3.9 million births and 9,500 to 11,500 neonatal deaths per cohort).
- **Prediction point:** 5 minutes after birth; only information known at birth.
- **Framework:** [`framework.md`](framework.md) (Spanish: [`framework_es.md`](framework_es.md)), version 1.0. Outcome card: [`docs/outcome_card_neonatal_nchs.md`](docs/outcome_card_neonatal_nchs.md).

## Data

The *Period/Cohort Linked Birth/Infant Death* files are downloaded from https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm and kept **outside the repository**, in the sibling folder `../NCHS_data/raw/` (one ZIP and one user guide per year); another location is set with the environment variable `NCHS_RAW_DIR`. They are public but are not redistributed: only the code is published. Their use is subject to the NCHS data use agreement: statistical analysis only, no attempt to identify persons and no linkage with identifiable data. Reports show no cell with fewer than 10 cases.

## Run order

| Order | Notebook | Creates | Framework stage |
|---|---|---|---|
| 1 | `notebooks/01_build_cohorts.ipynb` | `data/interim/cohort_<year>.parquet` (one per cohort) and `data/outputs_01_build_cohorts.txt` | S2 (data adapter) |

The reader is `libraries/nchs_reader.py`: it reads the fixed-width files directly from the ZIP files, with the positions of the record layout of the user guides (identical from 2016 to 2023).

## Repository structure

```
data/interim/    Cohorts in Parquet (not versioned)
data/            Aggregate outputs_*.txt
libraries/       Data adapter (fixed-width reader)
notebooks/       Adapter, count audit, models, validation and classification
docs/            Outcome card, framework figure
```

Notebooks and documents have a Spanish version with the `_es` suffix and the same code.

*Confidential: internal use of the research project.*
