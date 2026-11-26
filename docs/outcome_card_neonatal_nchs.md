# Outcome card — neonatal mortality, NCHS

Outcome card following the staged framework ([StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction)), version 1, 2026-11-20. Fields marked **pending** are fixed, and recorded in the decision log, before the gate that needs them. Spanish version: [`outcome_card_neonatal_nchs_es.md`](outcome_card_neonatal_nchs_es.md).

## 1. The question

With what the birth certificate records at delivery (the mother, the pregnancy, labor and delivery, and the newborn's condition at 5 minutes), **can live births at high risk of dying in their first 28 days be identified?**

Neonatal mortality covers, per WHO, deaths of live-born infants during the first 28 completed days of life (0 to 27 days). The death occurs after the prediction point, so the model predicts a future event rather than recognizing one that already happened. Perinatal mortality (fetal and early neonatal deaths) is addressed in another repository.

## 2. Identity

| Field | Value |
|---|---|
| Outcome | Neonatal death: death of a live-born infant before 28 days of life, taken from the linked death certificate (age at death 0 to 27 days; `AGER5X` 1–4) |
| Rung | First rung of the outcome ladder |
| Data source | NCHS (CDC) public-use *Linked Birth/Infant Death* files, birth-cohort version (section 7) |
| Unit and group | Live birth. The public files have no mother identifier, so the group is the birth itself (`group_id = unit_id`). Infants of the same multiple delivery cannot be linked; a declared limitation |
| Population | Live births to US-resident mothers (`RESTATUS` 1–3) with gestational age of **22 weeks or more** (`COMBGEST` 22–47), the lower viability bound used by WHO. Unknown gestational age (`99`): excluded, and the number is reported |
| Main label | Death between day 0 and day 27 of life |
| Sensitivity labels | (a) Death on days 2–27 among infants alive at the start of day 2 (48-hour landmark; originally 24 hours, changed by M4-D1, section 8); (b) early neonatal death, 0 to 6 days; (c) main label in the population of 28 weeks or more |
| Counts | Count audit, notebook 02 (2026-11-23): 29,829,867 live births in 8 cohorts (3.59–3.94 million each); 82,559 neonatal deaths (9,574–11,497 per cohort): 62,713 in development (2016–2021) and 19,846 in the temporal test (2022–2023). 46.6% of the deaths occur in the 0.59% of births at 22–27 weeks. Gate G1 passes |

## 3. Prediction point and information window (S6)

| Field | Value |
|---|---|
| Time zero | Birth |
| Prediction point | 5 minutes after birth, when the 5-minute Apgar exists |
| Allowed information | What is known at birth: maternal characteristics; obstetric history; prenatal care; smoking; risk factors and infections of the pregnancy; labor and delivery (induction, steroids, chorioamnionitis, presentation, route); plurality, sex, gestational age, birthweight, 5-minute Apgar and congenital anomalies identified at birth |
| Excluded | What happens or is recorded after the prediction point, or reflects the newborn's course: abnormal conditions of the newborn (assisted ventilation, ventilation over 6 hours, NICU admission, surfactant, antibiotics, seizures); 10-minute Apgar (later, and recorded only when the 5-minute score is below 6); infant transferred; infant living at time of report; breastfed at discharge; maternal morbidity of delivery (transfusion, laceration, uterine rupture, hysterectomy, intensive-care admission); every death-certificate variable |
| Values imputed by NCHS | Imputed birthweight and gestational age are kept with their flag (`BWTIMP`, `COMBGST_IMP`) |

## 4. Predictors (S7)

**Fixed on 2026-11-23** with the count audit (frequencies and missingness in the whole population, never split by outcome): **71 parameters** from the blocks below, without marital status (M4-D2); full list in `data/outputs_03_predictors_g2_g3.txt`. Blocks:

| Block | Candidates |
|---|---|
| Mother | Age; race and Hispanic origin; education; marital status; born in the US or abroad; payment source for the delivery; WIC |
| Obstetric history | Earlier births now living and now dead; other terminations or fetal deaths; interval since the last pregnancy; earlier cesareans; earlier preterm birth |
| Current pregnancy | Month prenatal care began and number of visits; smoking; pre-pregnancy BMI; weight gain; diabetes and hypertension (pre-existing and gestational), eclampsia; infertility treatment; infections (gonorrhea, syphilis, chlamydia, hepatitis B and C) |
| Labor and delivery | Induction; augmentation; steroids; antibiotics; chorioamnionitis; presentation; route and method of delivery; trial of labor; birthplace; attendant |
| Newborn | Plurality; sex; gestational age; birthweight; 5-minute Apgar; congenital anomalies (anencephaly, spina bifida, cyanotic heart disease, diaphragmatic hernia, omphalocele, gastroschisis, limb reduction, cleft lip and palate, Down syndrome, suspected chromosomal disorder, hypospadias) |

**Reference model fixed now:** gestational age and birthweight only. It is reported next to the full model to show how much the rest of the information adds, and not to credit the model with what prematurity already explains.

## 5. Sample size and learner (G3, S8)

| Field | Value |
|---|---|
| Events | 62,713 in development (2016–2021) and 19,846 in the temporal test (2022–2023). G3 passes the Riley et al. criteria in both steps (section 8) |
| Primary learner | **XGBoost**, chosen in the preliminary run with the framework rule (883 events per parameter); LR and the reference model as comparisons |
| Missing values | "Unknown or not stated" codes (`9`, `99`, `U`) become missing; median imputation without missingness indicators (M4-D3); complete records as a sensitivity analysis |
| Volume | About 3.6 million births per cohort. The adapter keeps only the needed columns, in Parquet |

## 5b. Sensitivity analyses

| Analysis | Question |
|---|---|
| 48-hour landmark (label a; M4-D1) | Does the result depend on deaths in the first hours, many in births without intent to resuscitate? |
| Population of 28 weeks or more (label c) | Does the model discriminate once extremely preterm births are removed? |
| Early neonatal death, 0 to 6 days (label b) | Does the result change if only the first week counts? |
| Reference model (gestational age and birthweight) | How much does the rest of the information add? |
| Cohorts 2020–2021 | Does the pandemic alter calibration? |

## 6. Classification criteria (G4)

| Criterion | How it applies | Status |
|---|---|---|
| C1, events already present | The death occurs after birth by design. Deaths in the first hour may reflect a situation already irreversible at birth; the 48-hour landmark (M4-D1) measures how much they weigh | Applicable through sensitivity (a) |
| C2, outcome with time | Age at death is in days; the event is after the prediction point | Applicable |
| C3, detection bias | The outcome comes from the death certificate, not from a test. Unlinked deaths (about 1%) remain as survivors; the linkage rate is reported | Not applicable; linkage declared |
| C4, stability over time | Development with cohorts 2016–2021 and temporal test with 2022–2023 | Applicable |

**Stated before the results.** Neonatal mortality models with gestational age, birthweight and Apgar usually exceed an AUROC of 0.85, largely because of very preterm births. That is why the reference model, the population of 28 weeks or more and the 24-hour landmark are fixed now (the landmark was moved to 48 hours by M4-D1, after the count audit and before any model was fitted). The framework's 0.75 threshold is not changed.

## 7. Data and conditions of use

- **Files:** *Period/Cohort Linked Birth/Infant Death*, 2017/2016 to 2024/2023, kept outside the repository in the shared folder `../NCHS_data/raw/` and downloaded from https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm. The birth cohort of year N is built from the births of year N and the deaths in years N and N+1 of infants born in N, joined by the cohort sequence number (`CO_SEQNUM`), as the user guide describes.
- **Why from the 2016 cohort:** first year in the user-created cohort format and with the 2003 revised certificate in every state.
- **Conditions (NCHS data use agreement):** use for statistical analysis only; no attempt to identify any person; no linkage with identifiable data. The data are not redistributed in the repository: the code that downloads and processes them is published. Reports show no cell with fewer than 10 cases.
- **No geography or day of birth** in the public files.

## 8. Next tasks

1. ~~Download of cohorts 2016–2023~~ (done).
2. ~~Data adapter~~ (done 2026-11-20: `libraries/nchs_reader.py`, `notebooks/01_build_cohorts.ipynb`; 100% of deaths joined to their birth).
3. ~~Count audit (S4)~~ (done 2026-11-23: `notebooks/02_count_audit.ipynb`, `data/outputs_02_count_audit.txt`). Findings that need a decision before the predictors are fixed:
   - **Age at death on day 1 changes coding between cohorts.** Deaths on day 1 fall from 1,412 (2016) to 845 (2017), 802 (2018) and about 430 from 2019 on, while deaths from day 2 on are stable. The 24-hour landmark (sensitivity a) would therefore not mean the same in development and in the temporal test.
   - **Marital status (`DMAR`) is not reported for about 12% of births from 2017 on** (0% in 2016): one state stopped reporting it. It is not comparable across cohorts and works as a proxy of the state.
   - **Interval since the last pregnancy (`ILP_R`)** is unknown in 11.6% (31% are first pregnancies, a valid category). Every other candidate has 3% or fewer unknowns.
   - **Gate G2 check:** the number of unknown fields alone gives an AUROC of 0.577 (0.556 at 28 weeks or more). All records are birth certificates, so there is no form-type signal as in the perinatal model, but the handling of unknowns must be fixed before fitting.
   Decisions taken with these findings, recorded on 2026-11-23 before any model is fitted (validated by Emmanuel Gutiérrez Jiménez; to be confirmed by the thesis supervisor):
   - **M4-D1:** sensitivity (a) moves from a 24-hour to a **48-hour landmark**: death on days 2–27 among the newborns alive at the start of day 2. It answers the same question for criterion C1 and does not depend on the coding change of day 1.
   - **M4-D2:** **marital status (`DMAR`) is excluded** from the candidates.
   - **M4-D3:** in the main model, unknowns are **imputed (median or mode of the development data) without missingness indicators**; complete records are a sensitivity analysis.
4. ~~Predictors, gates G2 and G3~~ (done 2026-11-23: `notebooks/03_predictors_g2_g3.ipynb`, `data/outputs_03_predictors_g2_g3.txt`). 71 parameters known at birth + 5 minutes. G2 passes the design checks; the number of unknown fields alone gives an AUROC of 0.601 in the development cohorts (0.571 at 28 weeks or more), which the main model does not see (M4-D3), and complete records remain a sensitivity analysis. G3 passes in both steps: development 22,578,517 births and 62,713 events (883 per parameter); observed Cox-Snell R² 0.0201 (53% of its maximum), 37,427 births and 104 events required. Reference model (gestational age + birthweight): R² 0.0142 (38% of its maximum).
5. ~~Preliminary run (S8)~~ (done 2026-11-23: `notebooks/04_preliminary_learners.ipynb`, `data/outputs_04_preliminary_learners.txt`). AUROC on the comparison part (12,543 events): LR 0.958, RF 0.960, ET 0.962, **XGBoost 0.964 (0.962–0.966)**; ensemble 0.963, 0.0007 below XGBoost (CI −0.0011 to −0.0003), not adopted. **Primary learner: XGBoost** (LR is 0.006 below, more than the 0.005 margin). Leakage diagnostic: XGBoost with its own missing-value handling gives 0.966, only 0.002 more.
6. ~~Formal evaluation, temporal validation, sensitivities and gate G4~~ (done 2026-11-23: `notebooks/05_main_evaluation.ipynb`, `data/outputs_05_main_evaluation.txt`).
   - **Internal validation (3 × 5, recalibrated):** XGBoost AUROC 0.964 (0.963–0.965), AUPRC 0.492, slope 0.98, observed/expected 0.99; the top 10% holds 91.5% of the deaths (9.1×). LR 0.958. Reference model (gestational age + birthweight) 0.907; the full model adds +0.057 (0.056–0.058).
   - **Temporal validation (2022–2023):** AUROC 0.961 (0.959–0.962), slope 1.01 (0.97–1.03), observed/expected 1.05 (1.01–1.08).
   - **C1 (48-hour landmark, on the model fitted once):** 34,466 of the 62,713 deaths (55%) occur on days 0 and 1. Among newborns alive at the start of day 2, the AUROC falls to 0.932 (drop 0.032; 0.031–0.033, within the 0.05 limit), but only 26% (25–27%) of the AUPRC gain is kept (67% required).
   - **Sensitivities:** 28 weeks or more 0.936 (reference 0.829 when refitted); 48 hours and 28 weeks or more 0.893; early neonatal 0.981; complete records 0.959 without refit and 0.960 refitted (imputation does not move the result); cohorts 2020–2021: AUROC 0.964 and observed/expected 0.94.
   - **Classification at G4 under framework 1.2: early identifier.** Meets C2 and C4; C3 not applicable; does not meet C1 because of the AUPRC gain: much of what the model detects are deaths in the first two days, largely determined at birth.
7. **Framework 1.3 (2026-11-23):** C1 is decided by the AUROC drop only, because the AUPRC gain depends on prevalence, which falls by more than half at 48 hours. Change adopted after seeing this result; no other model changes ([`decision_G4_C1_2026-11-23.md`](decision_G4_C1_2026-11-23.md)). With a drop of 0.032, C1 is met: **classification at G4: predictor** (`scripts/g4_framework_1_3.py`, `data/outputs_05b_g4_framework_1_3.txt`).

*Confidential: internal use of the research project.*
