# Mortalidad neonatal con datos NCHS

> **Framework.** Este repositorio aplica el framework por etapas para modelos de predicción clínica de la tesis. El framework (etapas, puertas, criterios y literatura) y el catálogo de modelos con su estado están en [StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction).

¿Se puede identificar, al nacer, a los nacidos vivos con riesgo alto de morir en sus primeros 28 días? Este modelo usa los archivos públicos de nacimientos vinculados con defunciones infantiles del National Center for Health Statistics (NCHS, CDC) y sigue el framework por etapas para modelos de predicción clínica.

> **Estado (26/11/2026): clasificado en P4 como predictor** (XGBoost, AUROC 0,964; a las 48 horas 0,932; temporal 0,961; [`data/outputs_05_main_evaluation.txt`](data/outputs_05_main_evaluation.txt); criterio C1: [`docs/decision_G4_C1_2026-11-23_es.md`](docs/decision_G4_C1_2026-11-23_es.md)). Las 8 cohortes de nacimiento (2016–2023) están construidas, con el 100% de las muertes infantiles unidas a su nacimiento ([`data/outputs_01_build_cohorts.txt`](data/outputs_01_build_cohorts.txt)); 82.559 muertes neonatales en 29,8 millones de nacidos vivos ([`data/outputs_02_count_audit.txt`](data/outputs_02_count_audit.txt)). Predictores fijados (71 parámetros) y puertas P2 y P3 superadas ([`data/outputs_03_predictors_g2_g3.txt`](data/outputs_03_predictors_g2_g3.txt)). Corrida preliminar: XGBoost es el algoritmo principal (AUROC 0,964; [`data/outputs_04_preliminary_learners.txt`](data/outputs_04_preliminary_learners.txt)). E10 hecha ([`docs/e10_action_neonatal_es.md`](docs/e10_action_neonatal_es.md)). Siguiente: reporte (E11).

[English version](README.md)

## Alcance

- **Desenlace:** muerte neonatal (0 a 27 días de vida).
- **Población:** nacidos vivos de madres residentes en EE. UU., de 22 semanas de gestación o más, cohortes de nacimiento 2016 a 2023 (unos 3,6 a 3,9 millones de nacimientos y 9.500 a 11.500 muertes neonatales por cohorte).
- **Punto de predicción:** 5 minutos después del nacimiento; solo información conocida al nacer.
- **Framework:** [StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction/blob/main/README_es.md) (inglés: [`README.md`](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction)); la versión vigente se mantiene solo allí. Ficha del desenlace: [`docs/outcome_card_neonatal_nchs_es.md`](docs/outcome_card_neonatal_nchs_es.md).

## Datos

Los archivos *Period/Cohort Linked Birth/Infant Death* se descargan de https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm y se guardan **fuera del repositorio**, en la carpeta hermana `../NCHS_data/raw/` (un ZIP y una guía de usuario por año); otra ubicación se indica con la variable de entorno `NCHS_RAW_DIR`. Son públicos, pero no se redistribuyen: solo se publica el código. Su uso está sujeto al acuerdo de uso de datos de NCHS: análisis estadístico únicamente, sin intentar identificar personas ni unir con datos identificables. Los reportes no muestran celdas con menos de 10 casos.

## Orden de ejecución

| Orden | Notebook | Crea | Etapa del framework |
|---|---|---|---|
| 1 | `notebooks/01_build_cohorts_es.ipynb` | `data/interim/cohort_<año>.parquet` (una por cohorte) y `data/outputs_01_build_cohorts.txt` | E2 (adaptador de datos) |
| 2 | `notebooks/02_count_audit_es.ipynb` | `data/outputs_02_count_audit.txt` | E4 (auditoría de conteos), P1, verificación P2 de los desconocidos |
| 3 | `notebooks/03_predictors_g2_g3_es.ipynb` | `data/contract/neonatal_nchs_v1/cohort_<año>.parquet` y `data/outputs_03_predictors_g2_g3.txt` | E7 (predictores), P2, P3 |
| 4 | `notebooks/04_preliminary_learners_es.ipynb` | `data/outputs_04_preliminary_learners.txt` y `data/outputs_04_selection.json` | E8 (corrida preliminar, regla del algoritmo principal) |
| 5 | `notebooks/05_main_evaluation_es.ipynb` | `data/outputs_05_main_evaluation.txt` y el modelo final en `models/` | E8–E9 (evaluación formal, validación temporal, sensibilidades), P4 |
| 6 | `notebooks/06_e10_action_es.ipynb` | `data/outputs_06_e10_action.txt` | E10 (carga de trabajo, subgrupos, qué impulsa el riesgo) |
| 6b | `scripts/tripod_flow_and_periods.py` | `data/outputs_tripod_flow_periods.txt` y `figures/tripod_flow_es.png` | E11 (ítems 20a y 20c de TRIPOD+AI: diagrama de flujo y comparación de períodos; lee las salidas del 01 y del 05 y la tabla contrato) |

El lector es `libraries/nchs_reader.py`: lee los archivos de ancho fijo directamente de los ZIP, con las posiciones del diseño de registro de las guías (idénticas de 2016 a 2023).

## Estructura del repositorio

```
data/interim/    Cohortes en Parquet (no se versionan)
data/            Salidas agregadas outputs_*.txt
libraries/       Adaptador de datos (lector de ancho fijo); neonatal_model.py: uso del modelo final guardado
models/          Modelo final del notebook 05 (pipeline en joblib, XGBoost en JSON, ficha del modelo); sin datos
notebooks/       Adaptador, auditoría de conteos, modelos, validación y clasificación
docs/            Ficha del desenlace, decisiones, guía de E10 y lista TRIPOD+AI
```

Notebooks y documentos tienen versión en español con el sufijo `_es` y el mismo código.

*Confidencial: uso interno del proyecto de investigación.*
