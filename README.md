# Neonatal mortality with NCHS data

> **Framework.** This repository applies the thesis's staged framework for clinical prediction models. The framework (stages, gates, criteria and literature) and the catalogue of models with their status are in [StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction).

Can live births at high risk of dying in their first 28 days be identified at birth? This model uses the public-use linked birth/infant death files of the National Center for Health Statistics (NCHS, CDC) and follows the staged framework for clinical prediction models.

> **Status (2026-11-23): classified at G4 as predictor under framework 1.3** (XGBoost, AUROC 0.964; at 48 hours 0.932; temporal 0.961; [`data/outputs_05_main_evaluation.txt`](data/outputs_05_main_evaluation.txt), [`data/outputs_05b_g4_framework_1_3.txt`](data/outputs_05b_g4_framework_1_3.txt)). Under framework 1.2 it was an early identifier ([`docs/decision_G4_C1_2026-11-23.md`](docs/decision_G4_C1_2026-11-23.md)). The 8 birth cohorts (2016–2023) are built, with 100% of infant deaths joined to their birth ([`data/outputs_01_build_cohorts.txt`](data/outputs_01_build_cohorts.txt)); 82,559 neonatal deaths in 29.8 million live births ([`data/outputs_02_count_audit.txt`](data/outputs_02_count_audit.txt)). Predictors fixed (71 parameters) and gates G2 and G3 passed ([`data/outputs_03_predictors_g2_g3.txt`](data/outputs_03_predictors_g2_g3.txt)). Preliminary run: XGBoost is the primary learner (AUROC 0.964; [`data/outputs_04_preliminary_learners.txt`](data/outputs_04_preliminary_learners.txt)). S10 done ([`docs/e10_action_neonatal.md`](docs/e10_action_neonatal.md)). Next: report (S11).

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
| 2 | `notebooks/02_count_audit.ipynb` | `data/outputs_02_count_audit.txt` | S4 (count audit), G1, G2 check of the unknowns |
| 3 | `notebooks/03_predictors_g2_g3.ipynb` | `data/contract/neonatal_nchs_v1/cohort_<year>.parquet` and `data/outputs_03_predictors_g2_g3.txt` | S7 (predictors), G2, G3 |
| 4 | `notebooks/04_preliminary_learners.ipynb` | `data/outputs_04_preliminary_learners.txt` and `data/outputs_04_selection.json` | S8 (preliminary run, primary-learner rule) |
| 5 | `notebooks/05_main_evaluation.ipynb` | `data/outputs_05_main_evaluation.txt` | S8–S9 (formal evaluation, temporal validation, sensitivities), G4 |
| 5b | `scripts/g4_framework_1_3.py` | `data/outputs_05b_g4_framework_1_3.txt` | G4 under framework 1.3 (no refit; reads the output of 05) |
| 6 | `notebooks/06_e10_action.ipynb` | `data/outputs_06_e10_action.txt` | S10 (workload, subgroups, drivers of risk) |

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
