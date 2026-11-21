# Ficha del desenlace — mortalidad neonatal, NCHS

Ficha del desenlace según el framework por etapas ([`../framework_es.md`](../framework_es.md)), versión 1, 20/11/2026. Los campos marcados **pendiente** se fijan, y se registran en el libro de decisiones, antes de la puerta que los necesita. Versión en inglés: [`outcome_card_neonatal_nchs.md`](outcome_card_neonatal_nchs.md).

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
| Etiquetas de sensibilidad | (a) Muerte entre el día 1 y el día 27 entre quienes sobreviven las primeras 24 horas (punto de referencia a las 24 h); (b) muerte neonatal precoz, de 0 a 6 días; (c) etiqueta principal en la población de 28 semanas o más |
| Conteos | **Pendiente**: se fijan en la auditoría de conteos (E4) |

## 3. Punto de predicción y ventana de información (E6)

| Campo | Valor |
|---|---|
| Tiempo cero | Nacimiento |
| Punto de predicción | 5 minutos después del nacimiento, cuando ya existe el Apgar de 5 minutos |
| Información permitida | Lo que se conoce al nacer: características de la madre; historia obstétrica; atención prenatal; tabaquismo; factores de riesgo e infecciones del embarazo; trabajo de parto y parto (inducción, esteroides, corioamnionitis, presentación, vía); pluralidad, sexo, edad gestacional, peso al nacer, Apgar a los 5 minutos y anomalías congénitas identificadas al nacer |
| Excluida | Lo que ocurre o se registra después del punto de predicción, o refleja el curso del recién nacido: condiciones anormales del recién nacido (ventilación asistida, ventilación por más de 6 horas, ingreso a cuidado intensivo neonatal, surfactante, antibióticos, convulsiones); Apgar a los 10 minutos (es posterior y solo se registra cuando el de 5 minutos es menor de 6); traslado del recién nacido; vivo al momento del reporte; lactancia al egreso; morbilidad materna del parto (transfusión, desgarro, ruptura uterina, histerectomía, ingreso a cuidado intensivo); todas las variables del certificado de defunción |
| Valores imputados por NCHS | Peso al nacer y edad gestacional imputados se conservan con su indicador (`BWTIMP`, `COMBGST_IMP`) |

## 4. Predictores (E7)

**Pendiente**: la lista definitiva se fija con la auditoría de conteos (frecuencias y faltantes en toda la población, nunca separadas por desenlace). Bloques candidatos:

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
| Eventos | Del orden de miles por cohorte; **pendiente** de la auditoría. La puerta P3 se verifica igual con los criterios de Riley et al. |
| Modelo principal | Se fija en E8 con la regla del framework según los eventos por parámetro; modelos de árboles y ensamble como comparaciones |
| Valores faltantes | **Pendiente**: códigos "desconocido o no informado" (`9`, `99`, `U`) pasan a faltante; el tratamiento se decide con la auditoría |
| Volumen | Unos 3,6 millones de nacimientos por cohorte. El adaptador guarda solo las columnas necesarias en Parquet |

## 5b. Análisis de sensibilidad

| Análisis | Pregunta |
|---|---|
| Punto de referencia a las 24 horas (etiqueta a) | ¿El resultado depende de las muertes en las primeras horas, muchas en nacimientos sin intención de reanimar? |
| Población de 28 semanas o más (etiqueta c) | ¿El modelo discrimina cuando se quitan los nacimientos extremadamente prematuros? |
| Muerte neonatal precoz de 0 a 6 días (etiqueta b) | ¿Cambia el resultado si solo se cuenta la primera semana? |
| Modelo de referencia (edad gestacional y peso) | ¿Cuánto agrega el resto de la información? |
| Cohortes 2020–2021 | ¿La pandemia altera la calibración? |

## 6. Criterios de clasificación (P4)

| Criterio | Cómo se aplica | Estado |
|---|---|---|
| C1, eventos ya presentes | La muerte ocurre después del nacimiento por diseño. Las muertes en la primera hora pueden reflejar una situación ya irreversible al nacer; el punto de referencia a las 24 horas mide cuánto pesan | Aplica mediante la sensibilidad (a) |
| C2, desenlace con tiempo | La edad al morir está en días; el evento es posterior al punto de predicción | Aplica |
| C3, sesgo de detección | El desenlace sale del certificado de defunción, no de un examen. Las muertes no vinculadas (alrededor del 1%) quedan como sobrevivientes; se reporta la tasa de vinculación | No aplica; se declara la vinculación |
| C4, estabilidad en el tiempo | Desarrollo con las cohortes 2016–2021 y prueba temporal con 2022–2023 | Aplica |

**Dicho antes de los resultados.** Los modelos de mortalidad neonatal con edad gestacional, peso al nacer y Apgar suelen superar una AUROC de 0,85, en buena parte por los nacimientos muy prematuros. Por eso se fijan desde ahora el modelo de referencia, la población de 28 semanas o más y el punto de referencia a las 24 horas. El umbral de 0,75 del framework no se cambia.

## 7. Datos y condiciones de uso

- **Archivos:** *Period/Cohort Linked Birth/Infant Death*, de 2017/2016 a 2024/2023, guardados fuera del repositorio en la carpeta compartida `../NCHS_data/raw/` y descargados de https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm. La cohorte de nacimiento del año N se arma con los nacimientos del año N y las muertes de los años N y N+1 de los nacidos en N, unidos por el número de secuencia de cohorte (`CO_SEQNUM`), como indica la guía de usuario.
- **Por qué desde la cohorte 2016:** es el primer año en formato de cohorte creada por el usuario y con el certificado revisado de 2003 en todos los estados.
- **Condiciones (acuerdo de uso de datos de NCHS):** uso solo para análisis estadístico; no intentar identificar a ninguna persona; no unir con datos identificables. Los datos no se redistribuyen en el repositorio: se publica el código que los descarga y procesa. En los reportes no se muestran celdas con menos de 10 casos.
- **Sin geografía ni día de nacimiento** en los archivos públicos.

## 8. Próximas tareas

1. ~~Descarga de las cohortes 2016–2023~~ (hecha).
2. ~~Adaptador de datos~~ (hecho el 20/11/2026: `libraries/nchs_reader.py`, `notebooks/01_build_cohorts_es.ipynb`; 100% de las muertes unidas a su nacimiento).
3. Auditoría de conteos (E4): población, eventos por etiqueta y cohorte, faltantes de cada candidato.
4. Fijar predictores y faltantes; puerta P3; modelo y clasificación.

*Confidencial: uso interno del proyecto de investigación.*
