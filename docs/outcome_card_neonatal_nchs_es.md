# Ficha del desenlace — mortalidad neonatal, NCHS

Ficha del desenlace según el framework por etapas ([StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction/blob/main/README_es.md)), versión 1, 20/11/2026. Los campos marcados **pendiente** se fijan, y se registran en el libro de decisiones, antes de la puerta que los necesita. Versión en inglés: [`outcome_card_neonatal_nchs.md`](outcome_card_neonatal_nchs.md).

## 1. La pregunta

Con lo que consta en el certificado de nacimiento al momento del parto (la madre, el embarazo, el trabajo de parto y el estado del recién nacido a los 5 minutos), **¿se puede identificar a los nacidos vivos con riesgo alto de morir en sus primeros 28 días?**

La mortalidad neonatal comprende, según la OMS, las muertes de nacidos vivos durante los primeros 28 días completos de vida (de 0 a 27 días). La muerte ocurre después del punto de predicción, de modo que el modelo predice un evento futuro y no reconoce uno que ya ocurrió. La mortalidad perinatal (muertes fetales y neonatales precoces) se trabaja en otro repositorio.

## 2. Identidad

| Campo | Valor |
|---|---|
| Desenlace | Muerte neonatal: muerte de un nacido vivo antes de cumplir 28 días de vida, tomada del certificado de defunción vinculado (edad al morir de 0 a 27 días; `AGER5X` 1–4) |
| Peldaño | Primer peldaño de la escalera de desenlaces |
| Fuente de datos | NCHS (CDC), archivos públicos *Linked Birth/Infant Death*, versión cohorte de nacimiento (sección 7) |
| Unidad y grupo | Nacido vivo. Los archivos públicos no traen identificador de la madre, así que el grupo es el propio nacimiento (`group_id = unit_id`). Los nacidos de un mismo parto múltiple no se pueden unir; es una limitación declarada |
| Población | Nacidos vivos de madres residentes en EE. UU. (`RESTATUS` 1–3) con edad gestacional de **22 semanas o más** (`COMBGEST` 22–47), límite inferior de viabilidad usado por la OMS. Edad gestacional desconocida (`99`): excluida, y se reporta cuántas son |
| Etiqueta principal | Muerte entre el día 0 y el día 27 de vida |
| Etiquetas de sensibilidad | (a) Muerte entre los días 2 y 27 en quienes están vivos al comenzar el día 2 (punto de referencia a las 48 h; originalmente 24 horas, cambiado por M4-D1, sección 8); (b) muerte neonatal precoz, de 0 a 6 días; (c) etiqueta principal en la población de 28 semanas o más |
| Conteos | Auditoría de conteos, notebook 02 (23/11/2026): 29.829.867 nacidos vivos en 8 cohortes (de 3,59 a 3,94 millones cada una); 82.559 muertes neonatales (de 9.574 a 11.497 por cohorte): 62.713 en desarrollo (2016–2021) y 19.846 en la prueba temporal (2022–2023). El 46,6% de las muertes ocurre en el 0,59% de los nacimientos de 22 a 27 semanas. La puerta P1 pasa |

## 3. Punto de predicción y ventana de información (E6)

| Campo | Valor |
|---|---|
| Tiempo cero | Nacimiento |
| Punto de predicción | 5 minutos después del nacimiento, cuando ya existe el Apgar de 5 minutos |
| Información permitida | Lo que se conoce al nacer: características de la madre; historia obstétrica; atención prenatal; tabaquismo; factores de riesgo e infecciones del embarazo; trabajo de parto y parto (inducción, esteroides, corioamnionitis, presentación, vía); pluralidad, sexo, edad gestacional, peso al nacer, Apgar a los 5 minutos y anomalías congénitas identificadas al nacer |
| Excluida | Lo que ocurre o se registra después del punto de predicción, o refleja el curso del recién nacido: condiciones anormales del recién nacido (ventilación asistida, ventilación por más de 6 horas, ingreso a cuidado intensivo neonatal, surfactante, antibióticos, convulsiones); Apgar a los 10 minutos (es posterior y solo se registra cuando el de 5 minutos es menor de 6); traslado del recién nacido; vivo al momento del reporte; lactancia al egreso; morbilidad materna del parto (transfusión, desgarro, ruptura uterina, histerectomía, ingreso a cuidado intensivo); todas las variables del certificado de defunción |
| Valores imputados por NCHS | Peso al nacer y edad gestacional imputados se conservan con su indicador (`BWTIMP`, `COMBGST_IMP`) |

## 4. Predictores (E7)

**Fijados el 23/11/2026** con la auditoría de conteos (frecuencias y faltantes en toda la población, nunca separadas por desenlace): **71 parámetros** de los bloques de abajo, sin el estado civil (M4-D2); lista completa en `data/outputs_03_predictors_g2_g3.txt`. Bloques:

| Bloque | Candidatos |
|---|---|
| Madre | Edad; raza y origen hispano; educación; estado civil; nacida en EE. UU. o fuera; fuente de pago del parto; WIC |
| Historia obstétrica | Hijos vivos y muertos anteriores; otras terminaciones o muertes fetales; intervalo desde el último embarazo; cesáreas anteriores; parto pretérmino anterior |
| Embarazo actual | Mes de inicio y número de controles prenatales; tabaquismo; IMC antes del embarazo; ganancia de peso; diabetes e hipertensión (previas y gestacionales), eclampsia; tratamiento de infertilidad; infecciones (gonorrea, sífilis, clamidia, hepatitis B y C) |
| Trabajo de parto y parto | Inducción; aumento; esteroides; antibióticos; corioamnionitis; presentación; vía y método del parto; intento de trabajo de parto; lugar del nacimiento; quién atendió |
| Recién nacido | Pluralidad; sexo; edad gestacional; peso al nacer; Apgar a los 5 minutos; anomalías congénitas (anencefalia, espina bífida, cardiopatía cianótica, hernia diafragmática, onfalocele, gastrosquisis, reducción de miembros, labio y paladar hendido, síndrome de Down, sospecha de alteración cromosómica, hipospadias) |

**Modelo de referencia fijado desde ahora:** solo edad gestacional y peso al nacer. Se reporta junto al modelo completo para mostrar cuánto agrega el resto de la información y no atribuirle al modelo lo que ya explica la prematurez.

## 5. Tamaño de muestra y modelo (P3, E8)

| Campo | Valor |
|---|---|
| Eventos | 62.713 en desarrollo (2016–2021) y 19.846 en la prueba temporal (2022–2023). P3 pasa con los criterios de Riley et al. en sus dos pasos (sección 8) |
| Modelo principal | **XGBoost**, elegido en la corrida preliminar con la regla del framework (883 eventos por parámetro); LR y modelo de referencia como comparaciones |
| Valores faltantes | Códigos "desconocido o no informado" (`9`, `99`, `U`) pasan a faltante; imputación por la mediana sin indicadores de faltante (M4-D3); registros completos como sensibilidad |
| Volumen | Unos 3,6 millones de nacimientos por cohorte. El adaptador guarda solo las columnas necesarias en Parquet |

## 5b. Análisis de sensibilidad

| Análisis | Pregunta |
|---|---|
| Punto de referencia a las 48 horas (etiqueta a; M4-D1) | ¿El resultado depende de las muertes en las primeras horas, muchas en nacimientos sin intención de reanimar? |
| Población de 28 semanas o más (etiqueta c) | ¿El modelo discrimina cuando se quitan los nacimientos extremadamente prematuros? |
| Muerte neonatal precoz de 0 a 6 días (etiqueta b) | ¿Cambia el resultado si solo se cuenta la primera semana? |
| Modelo de referencia (edad gestacional y peso) | ¿Cuánto agrega el resto de la información? |
| Cohortes 2020–2021 | ¿La pandemia altera la calibración? |

## 6. Criterios de clasificación (P4)

| Criterio | Cómo se aplica | Estado |
|---|---|---|
| C1, eventos ya presentes | La muerte ocurre después del nacimiento por diseño. Las muertes en la primera hora pueden reflejar una situación ya irreversible al nacer; el punto de referencia a las 48 horas (M4-D1) mide cuánto pesan | Aplica mediante la sensibilidad (a) |
| C2, desenlace con tiempo | La edad al morir está en días; el evento es posterior al punto de predicción | Aplica |
| C3, sesgo de detección | El desenlace sale del certificado de defunción, no de un examen. Las muertes no vinculadas (alrededor del 1%) quedan como sobrevivientes; se reporta la tasa de vinculación | No aplica; se declara la vinculación |
| C4, estabilidad en el tiempo | Desarrollo con las cohortes 2016–2021 y prueba temporal con 2022–2023 | Aplica |

**Dicho antes de los resultados.** Los modelos de mortalidad neonatal con edad gestacional, peso al nacer y Apgar suelen superar una AUROC de 0,85, en buena parte por los nacimientos muy prematuros. Por eso se fijan desde ahora el modelo de referencia, la población de 28 semanas o más y el punto de referencia a las 24 horas (el punto de referencia pasó a 48 horas por M4-D1, después de la auditoría de conteos y antes de ajustar cualquier modelo). El umbral de 0,75 del framework no se cambia.

## 7. Datos y condiciones de uso

- **Archivos:** *Period/Cohort Linked Birth/Infant Death*, de 2017/2016 a 2024/2023, guardados fuera del repositorio en la carpeta compartida `../NCHS_data/raw/` y descargados de https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm. La cohorte de nacimiento del año N se arma con los nacimientos del año N y las muertes de los años N y N+1 de los nacidos en N, unidos por el número de secuencia de cohorte (`CO_SEQNUM`), como indica la guía de usuario.
- **Por qué desde la cohorte 2016:** es el primer año en formato de cohorte creada por el usuario y con el certificado revisado de 2003 en todos los estados.
- **Condiciones (acuerdo de uso de datos de NCHS):** uso solo para análisis estadístico; no intentar identificar a ninguna persona; no unir con datos identificables. Los datos no se redistribuyen en el repositorio: se publica el código que los descarga y procesa. En los reportes no se muestran celdas con menos de 10 casos.
- **Sin geografía ni día de nacimiento** en los archivos públicos.

## 8. Próximas tareas

1. ~~Descarga de las cohortes 2016–2023~~ (hecha).
2. ~~Adaptador de datos~~ (hecho el 20/11/2026: `libraries/nchs_reader.py`, `notebooks/01_build_cohorts_es.ipynb`; 100% de las muertes unidas a su nacimiento).
3. ~~Auditoría de conteos (E4)~~ (hecha el 23/11/2026: `notebooks/02_count_audit_es.ipynb`, `data/outputs_02_count_audit.txt`). Hallazgos que requieren una decisión antes de fijar los predictores:
   - **La edad al morir en el día 1 cambia de codificación entre cohortes.** Las muertes del día 1 bajan de 1.412 (2016) a 845 (2017), 802 (2018) y unas 430 desde 2019, mientras que las muertes desde el día 2 son estables. El punto de referencia a las 24 horas (sensibilidad a) no significaría lo mismo en desarrollo y en la prueba temporal.
   - **El estado civil (`DMAR`) no se reporta en cerca del 12% de los nacimientos desde 2017** (0% en 2016): un estado dejó de informarlo. No es comparable entre cohortes y funciona como indicador del estado.
   - **El intervalo desde el último embarazo (`ILP_R`)** es desconocido en el 11,6% (el 31% son primeros embarazos, una categoría válida). Todos los demás candidatos tienen 3% o menos de desconocidos.
   - **Verificación de la puerta P2:** el número de campos desconocidos por sí solo da una AUROC de 0,577 (0,556 en 28 semanas o más). Todos los registros son certificados de nacimiento, así que no existe la señal del tipo de formulario del modelo perinatal, pero el manejo de los desconocidos debe fijarse antes de ajustar.
   Decisiones tomadas con estos hallazgos, registradas el 23/11/2026 antes de ajustar cualquier modelo (validadas por Emmanuel Gutiérrez Jiménez; por confirmar con el director de la tesis):
   - **M4-D1:** la sensibilidad (a) pasa de un punto de referencia a las 24 horas a uno a las **48 horas**: muerte entre los días 2 y 27 en los recién nacidos vivos al comenzar el día 2. Responde la misma pregunta para el criterio C1 y no depende del cambio de codificación del día 1.
   - **M4-D2:** **se excluye el estado civil (`DMAR`)** de los candidatos.
   - **M4-D3:** en el modelo principal los desconocidos se **imputan (mediana o moda de los datos de desarrollo) sin indicadores de faltante**; los registros completos son un análisis de sensibilidad.
4. ~~Predictores, puertas P2 y P3~~ (hecho el 23/11/2026: `notebooks/03_predictors_g2_g3_es.ipynb`, `data/outputs_03_predictors_g2_g3.txt`). 71 parámetros conocidos al nacer + 5 minutos. P2 pasa las verificaciones de diseño; el número de campos desconocidos por sí solo da una AUROC de 0,601 en las cohortes de desarrollo (0,571 en 28 semanas o más), que el modelo principal no ve (M4-D3), y los registros completos siguen como análisis de sensibilidad. P3 pasa en los dos pasos: desarrollo con 22.578.517 nacimientos y 62.713 eventos (883 por parámetro); R² de Cox-Snell observado 0,0201 (53% de su máximo); se requieren 37.427 nacimientos y 104 eventos. Modelo de referencia (edad gestacional + peso): R² 0,0142 (38% de su máximo).
5. ~~Corrida preliminar (E8)~~ (hecha el 23/11/2026: `notebooks/04_preliminary_learners_es.ipynb`, `data/outputs_04_preliminary_learners.txt`). AUROC en la parte de comparación (12.543 eventos): LR 0,958, RF 0,960, ET 0,962, **XGBoost 0,964 (0,962–0,966)**; ensamble 0,963, 0,0007 por debajo de XGBoost (IC −0,0011 a −0,0003), no adoptado. **Algoritmo principal: XGBoost** (la LR queda 0,006 por debajo, más que el margen de 0,005). Diagnóstico de fuga: XGBoost con su propio manejo de faltantes da 0,966, apenas 0,002 más.
6. ~~Evaluación formal, validación temporal, sensibilidades y puerta P4~~ (hecho el 23/11/2026: `notebooks/05_main_evaluation_es.ipynb`, `data/outputs_05_main_evaluation.txt`).
   - **Validación interna (3 × 5, recalibrada):** XGBoost AUROC 0,964 (0,963–0,965), AUPRC 0,492, pendiente 0,98, observados/esperados 0,99; el 10% superior concentra el 91,5% de las muertes (9,1×). LR 0,958. Modelo de referencia (edad gestacional + peso) 0,907; el modelo completo agrega +0,057 (0,056–0,058).
   - **Validación temporal (2022–2023):** AUROC 0,961 (0,959–0,962), pendiente 1,01 (0,97–1,03), observados/esperados 1,05 (1,01–1,08).
   - **C1 (punto de referencia a las 48 horas, sobre el modelo ajustado una sola vez):** 34.466 de las 62.713 muertes (55%) ocurren en los días 0 y 1. En los vivos al comenzar el día 2, la AUROC baja a 0,932 (caída 0,032; 0,031–0,033, dentro del límite de 0,05), pero solo se conserva el 26% (25–27%) de la ganancia de AUPRC (se exige 67%).
   - **Sensibilidades:** 28 semanas o más 0,936 (referencia 0,829 al reajustar); 48 horas y 28 semanas o más 0,893; neonatal precoz 0,981; registros completos 0,959 sin reajuste y 0,960 reajustado (la imputación no mueve el resultado); cohortes 2020–2021: AUROC 0,964 y observados/esperados 0,94.
   - **Clasificación en P4: predictor.** C1 cumple (caída del AUROC 0,032 ≤ 0,05; la parte conservada de la ganancia del AUPRC, 26%, se reporta y no decide: [`decision_G4_C1_2026-11-23_es.md`](decision_G4_C1_2026-11-23_es.md)), C2 y C4 cumplen, C3 no aplica. Buena parte de lo que el modelo detecta son muertes de los primeros dos días, ya definidas en buena medida al nacer; su uso se describe en [`e10_action_neonatal_es.md`](e10_action_neonatal_es.md).

*Confidencial: uso interno del proyecto de investigación.*
