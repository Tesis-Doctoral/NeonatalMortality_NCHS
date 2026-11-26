# Stage S11 — TRIPOD+AI checklist: NCHS neonatal model (M4)

Spanish version: [`tripod_ai_neonatal_nchs_es.md`](tripod_ai_neonatal_nchs_es.md). Checklist of TRIPOD+AI (Collins et al., BMJ 2024;385:e078378), item by item, with **where** each item is reported for model M4 (neonatal death 0–27 days, NCHS linked birth/infant death files, birth cohorts 2016–2023). Version of 2026-11-25.

The study **develops** the model (D: development 2016–2021, internal validation) and **evaluates** it (E: temporal test 2022–2023, same source). Item texts are summarized; the exact wording is in the official checklist.

**Status:** ✅ reported in the repository · 📝 to be written in the monograph or article (the content exists) · ⚠️ gap: something must be added · — not applicable (with the reason).

Abbreviations: **OC** = outcome card [`outcome_card_neonatal_nchs.md`](outcome_card_neonatal_nchs.md); **NB0x** = `notebooks/0x_*.ipynb`; **OUT0x** = `data/outputs_0x_*.txt`; **E10** = [`e10_action_neonatal.md`](e10_action_neonatal.md); **FW** = framework ([StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction)).

## Title and abstract

| Item | D/E | Content | Where | Status |
|---|---|---|---|---|
| 1 | D;E | Development and evaluation of a multivariable model, population, outcome | Monograph chapter / article title: "development and temporal validation… neonatal death… live births in the United States" | 📝 |
| 2 | D;E | Abstract following TRIPOD+AI for abstracts | Monograph / article | 📝 |

## Introduction

| Item | D/E | Content | Where | Status |
|---|---|---|---|---|
| 3a | D;E | Healthcare context and rationale; existing models | OC §1; literature in the monograph (models with gestational age, weight and Apgar usually exceed AUROC 0.85: OC §6) | 📝 |
| 3b | D;E | Target population, place in the care pathway, intended users | OC §1–§3 (live births ≥ 22 weeks, 5 minutes after birth); E10 §1 (neonatology, prioritization of care) | ✅ |
| 3c | D;E | Known health inequalities between groups | E10 §3 (neonatal mortality 4.4 vs 2.3 per 1,000 for Black vs White mothers); literature in the monograph | 📝 |
| 4 | D;E | Objectives: develop, evaluate or both | OC §1; README (scope) | ✅ |

## Methods

| Item | D/E | Content | Where | Status |
|---|---|---|---|---|
| 5a | D;E | Data sources for development and evaluation, representativeness | OC §2, §7; README (data). Same source for both: national vital statistics, all US live births | ✅ |
| 5b | D;E | Dates of the data | OC §2, §7: birth cohorts 2016–2021 (development) and 2022–2023 (test); deaths up to the first birthday | ✅ |
| 6a | D;E | Setting, number and location of centres | OC §2, §7: whole US population, all states; the public files have no geography or hospital | ✅ |
| 6b | D;E | Eligibility criteria | OC §2 (US residents, `COMBGEST` 22–47, unknown gestational age excluded); NB02 (Q-N1, Q-N3) | ✅ |
| 6c | D;E | Treatments received and how they were handled | Care before the prediction point enters as predictors (steroids, antibiotics, induction, route of delivery: OC §4); care after the prediction point is excluded (OC §3; NB03 E6) | ✅ |
| 7 | D;E | Data preparation and quality control, similarity between groups | `libraries/nchs_reader.py`; NB01 (linkage 100%); NB02 (unknowns by cohort, decisions M4-D1, M4-D2); E10 §3 (unknown race) | ✅ |
| 8a | D;E | Outcome, horizon, how and when it was assessed | OC §2: death 0–27 days from the linked death certificate; NB02 (age at death, M4-D1) | ✅ |
| 8b | D;E | Subjective assessment of the outcome | — Death is objective (certificate linkage) | — |
| 8c | D;E | Blinding of outcome assessment | — Death certificates are filled in without the model; linkage is automatic by NCHS | — |
| 9a | D | Initial choice of predictors and preselection | OC §4 (blocks fixed with the count audit, never split by outcome); M4-D2 (marital status excluded) | ✅ |
| 9b | D;E | Definition of every predictor, how and when measured | NB03 (`make_predictors`, table of the 71 parameters with their NCHS field); OC §3 (birth + 5 minutes) | ✅ |
| 9c | D;E | Subjective assessment of predictors | 5-minute Apgar is assessed by the birth attendant; state it in the monograph | 📝 |
| 10 | D;E | Sample size, development and evaluation | NB03 gate G3 (Riley et al., two steps; 62,713 events vs 104 required); OUT03 | ✅ |
| 11 | D;E | Missing data | M4-D3 (median imputation without indicators); NB03 E7 (% missing per parameter); NB05 (complete records, with and without refit) | ✅ |
| 12a | D | Use of the data: partitions, no leakage | NB04 (80/20 split), NB05 (3 × 5 cross-validation, temporal split by cohort); NB03 gate G2 (design checks) | ✅ |
| 12b | D | Handling of predictors (form, scaling, categories) | NB03 (`make_predictors`: reference levels, collapsed categories); scaling inside the LR pipeline | ✅ |
| 12c | D | Model type, building steps, hyperparameter tuning, internal validation | NB04 (random search, 3 inner folds, ensemble, primary-learner rule); NB05 (3 × 5 CV with Platt recalibration inside training) | ✅ |
| 12d | D;E | Heterogeneity between clusters | No hospital or geography in the files; heterogeneity over time by cohort (2020–2021 vs 2016–2019, NB05; 2022 vs 2023, NB06) | ✅ |
| 12e | D;E | Performance measures and model comparison | NB05: AUROC, AUPRC, Brier, calibration slope and intercept, O/E, ECE, decision curve, accuracy and F1 at operating points; paired bootstrap vs reference model | ✅ |
| 12f | E | Model updating after evaluation | No updating on the temporal test: model fitted once on 2016–2021 (Platt recalibration is part of development) | ✅ |
| 12g | E | How predictions were calculated in the evaluation | NB05/NB06 code; final model in `models/` and `libraries/neonatal_model.py` (predictions reproduced from the saved files, checked in NB05) | ✅ |
| 13 | D;E | Class imbalance methods | Case-control sample (all events + 2% of non-events) with weights 1/0.02 and Platt recalibration, so that probabilities and metrics refer to the whole population (NB04, NB05) | ✅ |
| 14 | D;E | Approach to fairness | E10 §3 and NB06: subgroups (race and Hispanic origin, payment, plurality, cohort) with flags fixed before running | ✅ |
| 15 | D | Model output, thresholds and how they were chosen | Probability of death 0–27 days; operating points in NB06 and E10 §2 (risk ≥ 1% recommended by workload) | ✅ |
| 16 | D;E | Differences between development and evaluation data | Same source, definitions and predictors; only the cohort years differ (OC §2). Coding change of day-1 deaths handled by M4-D1 | ✅ |
| 17 | D;E | Ethics approval and consent | [`ethics_statement_neonatal.md`](ethics_statement_neonatal.md): public de-identified data under the NCHS conditions of use; not human subjects research (45 CFR 46.102); research without risk (Colombian Resolution 8430 of 1993, art. 11); consent not applicable. Missing only the decision of the Uninorte ethics committee (minute and date) | ✅ (committee decision pending) |

## Open science

| Item | D/E | Content | Where | Status |
|---|---|---|---|---|
| 18a | D;E | Funding | Monograph | 📝 |
| 18b | D;E | Conflicts of interest | Monograph | 📝 |
| 18c | D;E | Protocol and deviations | FW (staged framework) + OC (dated decisions); deviations recorded: M4-D1 to M4-D3, framework 1.3 ([`decision_G4_C1_2026-11-23.md`](decision_G4_C1_2026-11-23.md)) | ✅ |
| 18d | D;E | Registration | Not registered; state it | 📝 |
| 18e | D;E | Data availability | Public NCHS files, download link and conditions (OC §7, README); not redistributed | ✅ |
| 18f | D;E | Code availability, software and versions | GitHub (Tesis-Doctoral/NeonatalMortality_NCHS), MIT license, `requirements.txt` with exact versions (Python 3.11.9) | ✅ |
| 19 | D;E | Patient and public involvement | None; state it | 📝 |

## Results

| Item | D/E | Content | Where | Status |
|---|---|---|---|---|
| 20a | D;E | Flow of participants, with and without the outcome | `figures/tripod_flow.png` (flow diagram by period: births in the files, exclusions, analysed population with deaths, model sample) and `data/outputs_tripod_flow_periods.txt`; `scripts/tripod_flow_and_periods.py` | ✅ |
| 20b | D;E | Characteristics of the data, predictors, missing values | OUT03 (Q-P1: % missing and mean or % yes of the 71 parameters); OUT02 | ✅ |
| 20c | E | Development vs evaluation distributions | `data/outputs_tripod_flow_periods.txt`: outcome and 30 main predictors in development vs temporal test, with % unknown and standardized difference; only smoking during pregnancy differs by |d| ≥ 0.10 (6.1% vs 3.3%) | ✅ |
| 21 | D;E | Participants and events in every analysis | NB04 (fit/tune and comparison parts), NB05 (development and temporal samples, events of every sensitivity), NB06 | ✅ |
| 22 | D | Full model specification (formula, code, object) | Code and hyperparameters (`data/outputs_04_selection.json`); fitted model in `models/` (joblib pipeline, XGBoost JSON, card with predictor order, imputation medians and Platt coefficients) | ✅ |
| 23a | D;E | Performance with CI, subgroups, plots | OUT05 (CI of every metric), figures (ROC, confusion matrices); subgroups in NB06 with bootstrap 95% CI of AUROC and O/E | ✅ |
| 23b | D;E | Heterogeneity between clusters | By cohort (NB05, NB06) | ✅ |
| 24 | E | Results of model updating | — No updating | — |

## Discussion and use

| Item | D/E | Content | Where | Status |
|---|---|---|---|---|
| 25 | D;E | Overall interpretation, including fairness | E10 §1–§4; OC §8 point 6–7 (what the model detects: deaths in the first two days); monograph | 📝 |
| 26 | D;E | Limitations | E10 §6; OC §2 (multiple births not linked, ~1% unlinked deaths) | ✅ |
| 27a | D | Poor-quality or missing input data in use | E10 §5 (data at 5 minutes; unknown race underestimated) | ✅ |
| 27b | D | Users' interaction and expertise | E10 §1, §5 (neonatology; threshold according to capacity) | ✅ |
| 27c | D;E | Future research | E10 §5 (local validation and recalibration, e.g. Colombia); monograph | 📝 |

## Gaps to close before the report

1. ✅ *Done (2026-11-26; NB05 run, reloaded files reproduce the predictions exactly).* **Saved model (items 12g and 22).** Notebook 05 should save the fitted primary model (XGBoost in JSON and the Platt calibrator) in `models/`, with a short example of how to predict a new birth. The data cannot be shared, but the model can.
2. ✅ *Done (2026-11-26).* **Pinned versions (18f).** `requirements.txt` lists packages without versions; add the exact versions used (Python, numpy, pandas, scikit-learn, xgboost) with `pip freeze` from the environment that ran the notebooks.
3. ✅ *Done (2026-11-26): `scripts/tripod_flow_and_periods.py`.* **Flow diagram and comparison of periods (20a, 20c).** One figure with the flow from all live births to the analysed population, by period; and a table of the main predictors and the outcome in development vs temporal test.
4. ✅ *Statement written (2026-11-26): `docs/ethics_statement_neonatal.md`; only the Uninorte committee decision is missing.* **Ethics (17).** Statement that the study uses public de-identified data; confirm with Uninorte whether an exemption letter from the ethics committee is needed.
5. ✅ *Done (2026-11-26; NB06 run).* **Confidence intervals by subgroup (23a).** Bootstrap CI for the AUROC and O/E of each subgroup in NB06.

*Confidential: internal use of the research project.*
