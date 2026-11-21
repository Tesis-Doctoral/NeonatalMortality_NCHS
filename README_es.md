# Mortalidad neonatal con datos NCHS

> **Framework.** Este repositorio aplica el framework por etapas para modelos de predicción clínica de la tesis. El framework (etapas, puertas, criterios y literatura) y el catálogo de modelos con su estado están en [StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction).

¿Se puede identificar, al nacer, a los nacidos vivos con riesgo alto de morir en sus primeros 28 días? Este modelo usa los archivos públicos de nacimientos vinculados con defunciones infantiles del National Center for Health Statistics (NCHS, CDC) y sigue el framework por etapas para modelos de predicción clínica.

> **Estado (20/11/2026): adaptador de datos hecho.** Las 8 cohortes de nacimiento (2016–2023) están construidas, con el 100% de las muertes infantiles unidas a su nacimiento ([`data/outputs_01_build_cohorts.txt`](data/outputs_01_build_cohorts.txt)). Siguiente: auditoría de conteos.

[English version](README.md)

## Alcance

- **Desenlace:** muerte neonatal (0 a 27 días de vida).
- **Población:** nacidos vivos de madres residentes en EE. UU., de 22 semanas de gestación o más, cohortes de nacimiento 2016 a 2023 (unos 3,6 a 3,9 millones de nacimientos y 9.500 a 11.500 muertes neonatales por cohorte).
- **Punto de predicción:** 5 minutos después del nacimiento; solo información conocida al nacer.
- **Framework:** [`framework_es.md`](framework_es.md) (inglés: [`framework.md`](framework.md)), versión 1.0. Ficha del desenlace: [`docs/outcome_card_neonatal_nchs_es.md`](docs/outcome_card_neonatal_nchs_es.md).

## Datos

Los archivos *Period/Cohort Linked Birth/Infant Death* se descargan de https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm y se guardan **fuera del repositorio**, en la carpeta hermana `../NCHS_data/raw/` (un ZIP y una guía de usuario por año); otra ubicación se indica con la variable de entorno `NCHS_RAW_DIR`. Son públicos, pero no se redistribuyen: solo se publica el código. Su uso está sujeto al acuerdo de uso de datos de NCHS: análisis estadístico únicamente, sin intentar identificar personas ni unir con datos identificables. Los reportes no muestran celdas con menos de 10 casos.

## Orden de ejecución

| Orden | Notebook | Crea | Etapa del framework |
|---|---|---|---|
| 1 | `notebooks/01_build_cohorts_es.ipynb` | `data/interim/cohort_<año>.parquet` (una por cohorte) y `data/outputs_01_build_cohorts.txt` | E2 (adaptador de datos) |

El lector es `libraries/nchs_reader.py`: lee los archivos de ancho fijo directamente de los ZIP, con las posiciones del diseño de registro de las guías (idénticas de 2016 a 2023).

## Estructura del repositorio

```
data/interim/    Cohortes en Parquet (no se versionan)
data/            Salidas agregadas outputs_*.txt
libraries/       Adaptador de datos (lector de ancho fijo)
notebooks/       Adaptador, auditoría de conteos, modelos, validación y clasificación
docs/            Ficha del desenlace, figura del framework
```

Notebooks y documentos tienen versión en español con el sufijo `_es` y el mismo código.

*Confidencial: uso interno del proyecto de investigación.*
