# Stage S10 — from classification to action: NCHS neonatal model (M4)

Spanish version: [`e10_action_neonatal_es.md`](e10_action_neonatal_es.md). Results: `notebooks/06_e10_action.ipynb`, `data/outputs_06_e10_action.txt` (2026-11-24). All figures are from the **temporal test 2022–2023** (7,251,350 live births and 19,846 neonatal deaths), with the model fitted once on 2016–2021. AUROC 0.961.

## 1. Class and use

The model is a **predictor** (framework 1.3): at 5 minutes after birth it estimates the risk of dying in the first 28 days. Its use is **prevention: prioritizing the highest-risk newborns for more intensive care from birth**, for example:

- immediate assessment by neonatology and an early decision on the level of care (intensive care unit, transfer to a higher-level center);
- close monitoring during the first days and before discharge;
- follow-up after discharge during the first month.

It does not replace clinical judgment: it ranks newborns so that care reaches the highest-risk ones first.

## 2. Operating point and workload

| Operating point | Flagged per 1,000 births | Sensitivity | Specificity | PPV | Alerts per death found |
|---|---|---|---|---|---|
| Top 1% of risk | 10 | 0.747 | 0.992 | 0.205 | 4.9 |
| **Risk ≥ 1%** | **19** | **0.818** | **0.983** | **0.118** | **8.5** |
| Top 2% of risk | 20 | 0.822 | 0.982 | 0.113 | 8.9 |
| Top 10% of risk | 100 | 0.904 | 0.902 | 0.025 | 40.4 |

**Recommendation: risk of 1% or more.** It flags about 19 of every 1,000 live births, finds 82% of neonatal deaths and requires about 8 or 9 alerts per death found, a workload compatible with an assessment by neonatology. The top 10% finds more deaths (90%) but with 40 alerts per death.

**After the first 48 hours** (newborns alive at the start of day 2, where preventive care still has time to act), the same 1% cut flags 18 of every 1,000, finds 70% of the deaths on days 2 to 27 and requires about 19 alerts per death found. The model remains useful in that group, with a higher workload per case.

**Original objective of the thesis** (sensitivity and specificity above 0.75): met. At the point where both are equal they are 0.904 (risk cut 0.12%); among newborns alive at day 2, 0.856. If sensitivity of 0.75 is required, specificity is 0.992.

## 3. Equity: performance by subgroup

Flags fixed before running: AUROC more than 0.05 below the whole population (below 0.911) or observed/expected outside 0.80–1.25.

| Group | AUROC | Observed/expected | Sensitivity at the top-10% cut |
|---|---|---|---|
| Mother's race and Hispanic origin | 0.942 (other) to 0.965 (Hispanic, Asian) | 0.96 to 1.09 | 0.87 to 0.92 |
| Payment of the delivery | 0.949 (Medicaid) to 0.972 (other) | 0.98 to 1.22 | 0.89 to 0.94 |
| Plurality | 0.958 to 0.971 | 1.04 to 1.20 | 0.89 to 1.00 |
| Cohort 2022 / 2023 | 0.960 / 0.961 | 1.03 / 1.06 | 0.90 / 0.91 |

- **No group has a discrimination flag.** The lowest AUROCs (race "other" 0.942; Medicaid 0.949; Black mothers 0.954) remain well above the limit.
- **Calibration:** one flag, for mothers with unknown race (O/E 1.45, about 64,000 births): the model underestimates their risk. Its 95% bootstrap CI (1.20–1.73) reaches the 1.25 limit, so the flag is reported as not confirmed (imprecise); every subgroup has a lower AUROC limit of 0.93 or more (notebook 06). The missing value may reflect incomplete records of higher-risk deliveries; it should be checked locally before use.
- **Share flagged:** Black mothers are flagged more often (16.1%) than White mothers (9.1%). This matches their higher neonatal mortality (4.4 vs 2.3 per 1,000) with the same calibration, so it reflects a real difference in risk rather than a bias of the model.

## 4. What drives the risk (descriptive, not causal)

| Type of predictor | Contribution (SHAP) |
|---|---|
| Condition at birth: 5-minute Apgar (40.5%), birthweight (22.9%), gestational age (4.5%) | 68% |
| Related to prenatal or delivery care | 13.5% |
| Other (mother, obstetric history, congenital anomalies, plurality) | 19% |

Among the care-related factors, the largest are cesarean delivery (3.0%), number of prenatal visits (2.6%), BMI (1.3%), late start of prenatal care (1.2%), weight gain (0.9%), WIC (0.9%), birth out of hospital (0.8%) and smoking during pregnancy (0.7%).

Two readings for the prevention strategy:

- **At 5 minutes after birth, the risk is already largely set** by prematurity, weight and the newborn's condition. The model serves to act quickly on that risk, not to avoid it.
- **The prevention that lowers that risk happens before delivery:** early and sufficient prenatal care, control of smoking and nutritional status, and delivery in a place with the appropriate level of care. These factors are associated with risk, but their contribution is not causal (a cesarean, for example, is usually a response to a complication, not its cause).

## 5. Conditions to implement it in a health entity

1. **Local validation and recalibration.** The model was developed with US vital statistics. Before using it in another country, such as Colombia, it must be validated with local data and at least its intercept recalibrated, because baseline neonatal mortality differs.
2. **Data available at 5 minutes.** It needs the birth-certificate or clinical-record data at that moment: gestational age, weight, Apgar, plurality, anomalies, history and pregnancy and delivery data.
3. **Threshold according to capacity.** The 1% cut implies about 19 priority assessments per 1,000 births. An entity with less capacity can use the top 1% of risk (10 per 1,000, 75% of the deaths).
4. **Monitoring.** Review calibration and subgroup performance every year, especially in groups with incomplete data.

## 6. Limitations

- Administrative certificate data: no detailed clinical variables (laboratory, ultrasound, fetal monitoring).
- No geography in the public-use files: performance by region or by the hospital's level of care cannot be assessed.
- The contribution of the predictors is descriptive; it does not show that changing a factor changes the risk.
