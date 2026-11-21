# Outcome card — neonatal mortality, NCHS

Outcome card following the staged framework ([`../framework.md`](../framework.md)), version 1, 2026-11-20. Fields marked **pending** are fixed, and recorded in the decision log, before the gate that needs them. Spanish version: [`outcome_card_neonatal_nchs_es.md`](outcome_card_neonatal_nchs_es.md).

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
| Sensitivity labels | (a) Death between day 1 and day 27 among infants surviving the first 24 hours (24-hour landmark); (b) early neonatal death, 0 to 6 days; (c) main label in the population of 28 weeks or more |
| Counts | **Pending**: fixed in the count audit (S4) |

## 3. Prediction point and information window (S6)

| Field | Value |
|---|---|
| Time zero | Birth |
| Prediction point | 5 minutes after birth, when the 5-minute Apgar exists |
| Allowed information | What is known at birth: maternal characteristics; obstetric history; prenatal care; smoking; risk factors and infections of the pregnancy; labor and delivery (induction, steroids, chorioamnionitis, presentation, route); plurality, sex, gestational age, birthweight, 5-minute Apgar and congenital anomalies identified at birth |
| Excluded | What happens or is recorded after the prediction point, or reflects the newborn's course: abnormal conditions of the newborn (assisted ventilation, ventilation over 6 hours, NICU admission, surfactant, antibiotics, seizures); 10-minute Apgar (later, and recorded only when the 5-minute score is below 6); infant transferred; infant living at time of report; breastfed at discharge; maternal morbidity of delivery (transfusion, laceration, uterine rupture, hysterectomy, intensive-care admission); every death-certificate variable |
| Values imputed by NCHS | Imputed birthweight and gestational age are kept with their flag (`BWTIMP`, `COMBGST_IMP`) |

## 4. Predictors (S7)

**Pending**: the final list is fixed with the count audit (frequencies and missingness in the whole population, never split by outcome). Candidate blocks:

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
| Events | Thousands per cohort; **pending** the audit. Gate G3 is still checked with the Riley et al. criteria |
| Primary learner | Fixed in S8 with the framework rule on events per parameter; tree models and the ensemble as comparisons |
| Missing values | **Pending**: "unknown or not stated" codes (`9`, `99`, `U`) become missing; the handling is decided with the audit |
| Volume | About 3.6 million births per cohort. The adapter keeps only the needed columns, in Parquet |

## 5b. Sensitivity analyses

| Analysis | Question |
|---|---|
| 24-hour landmark (label a) | Does the result depend on deaths in the first hours, many in births without intent to resuscitate? |
| Population of 28 weeks or more (label c) | Does the model discriminate once extremely preterm births are removed? |
| Early neonatal death, 0 to 6 days (label b) | Does the result change if only the first week counts? |
| Reference model (gestational age and birthweight) | How much does the rest of the information add? |
| Cohorts 2020–2021 | Does the pandemic alter calibration? |

## 6. Classification criteria (G4)

| Criterion | How it applies | Status |
|---|---|---|
| C1, events already present | The death occurs after birth by design. Deaths in the first hour may reflect a situation already irreversible at birth; the 24-hour landmark measures how much they weigh | Applicable through sensitivity (a) |
| C2, outcome with time | Age at death is in days; the event is after the prediction point | Applicable |
| C3, detection bias | The outcome comes from the death certificate, not from a test. Unlinked deaths (about 1%) remain as survivors; the linkage rate is reported | Not applicable; linkage declared |
| C4, stability over time | Development with cohorts 2016–2021 and temporal test with 2022–2023 | Applicable |

**Stated before the results.** Neonatal mortality models with gestational age, birthweight and Apgar usually exceed an AUROC of 0.85, largely because of very preterm births. That is why the reference model, the population of 28 weeks or more and the 24-hour landmark are fixed now. The framework's 0.75 threshold is not changed.

## 7. Data and conditions of use

- **Files:** *Period/Cohort Linked Birth/Infant Death*, 2017/2016 to 2024/2023, kept outside the repository in the shared folder `../NCHS_data/raw/` and downloaded from https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm. The birth cohort of year N is built from the births of year N and the deaths in years N and N+1 of infants born in N, joined by the cohort sequence number (`CO_SEQNUM`), as the user guide describes.
- **Why from the 2016 cohort:** first year in the user-created cohort format and with the 2003 revised certificate in every state.
- **Conditions (NCHS data use agreement):** use for statistical analysis only; no attempt to identify any person; no linkage with identifiable data. The data are not redistributed in the repository: the code that downloads and processes them is published. Reports show no cell with fewer than 10 cases.
- **No geography or day of birth** in the public files.

## 8. Next tasks

1. ~~Download of cohorts 2016–2023~~ (done).
2. ~~Data adapter~~ (done 2026-11-20: `libraries/nchs_reader.py`, `notebooks/01_build_cohorts.ipynb`; 100% of deaths joined to their birth).
3. Count audit (S4): population, events per label and cohort, missingness of every candidate.
4. Fix predictors and missing values; gate G3; model and classification.

*Confidential: internal use of the research project.*
