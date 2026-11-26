# Etapa E10 — de la clasificación a la acción: modelo neonatal NCHS (M4)

Versión en inglés: [`e10_action_neonatal.md`](e10_action_neonatal.md). Resultados: `notebooks/06_e10_action_es.ipynb`, `data/outputs_06_e10_action.txt` (24/11/2026). Todas las cifras son de la **prueba temporal 2022–2023** (7.251.350 nacidos vivos y 19.846 muertes neonatales), con el modelo ajustado una sola vez con 2016–2021. AUROC 0,961.

## 1. Clase y uso

El modelo es **predictor**: estima, a los 5 minutos del nacimiento, el riesgo de morir en los primeros 28 días. El uso que le corresponde es **la prevención: priorizar a los recién nacidos de mayor riesgo para una atención más intensa desde el nacimiento**, por ejemplo:

- valoración inmediata por neonatología y decisión temprana sobre el nivel de cuidado (unidad de cuidado intensivo, traslado a un centro de mayor complejidad);
- vigilancia estrecha durante los primeros días y antes del egreso;
- seguimiento después del egreso en el primer mes.

No sustituye el juicio clínico: ordena a los recién nacidos para que la atención llegue antes a los de mayor riesgo.

## 2. Punto de operación y carga de trabajo

| Punto de operación | Marcados por 1.000 nacimientos | Sensibilidad | Especificidad | VPP | Alertas por muerte encontrada |
|---|---|---|---|---|---|
| 1% de mayor riesgo | 10 | 0,747 | 0,992 | 0,205 | 4,9 |
| **Riesgo ≥ 1%** | **19** | **0,818** | **0,983** | **0,118** | **8,5** |
| 2% de mayor riesgo | 20 | 0,822 | 0,982 | 0,113 | 8,9 |
| 10% de mayor riesgo | 100 | 0,904 | 0,902 | 0,025 | 40,4 |

**Recomendación: riesgo de 1% o más.** Marca a unos 19 de cada 1.000 nacidos vivos, encuentra el 82% de las muertes neonatales y exige unas 8 o 9 alertas por cada muerte encontrada. Es una carga compatible con una valoración por neonatología. El 10% de mayor riesgo encuentra más muertes (90%), pero con 40 alertas por cada una.

**Después de las primeras 48 horas** (vivos al comenzar el día 2, donde el cuidado preventivo todavía tiene tiempo de actuar), el mismo corte de 1% marca a 18 de cada 1.000, encuentra el 70% de las muertes de los días 2 a 27 y exige unas 19 alertas por muerte encontrada. El modelo sigue siendo útil en ese grupo, con más carga por caso.

**Objetivo original de la tesis** (sensibilidad y especificidad mayores de 0,75): se cumple. En el punto donde las dos son iguales valen 0,904 (corte de riesgo 0,12%); en los vivos al día 2, 0,856. Si se exige sensibilidad de 0,75, la especificidad es 0,992.

## 3. Equidad: desempeño por subgrupos

Alertas fijadas antes de correr: AUROC más de 0,05 por debajo del total (por debajo de 0,911) u observados/esperados fuera de 0,80–1,25.

| Grupo | AUROC | Observados/esperados | Sensibilidad en el corte del 10% |
|---|---|---|---|
| Raza y origen de la madre | 0,942 (otra) a 0,965 (hispana, asiática) | 0,96 a 1,09 | 0,87 a 0,92 |
| Forma de pago | 0,949 (Medicaid) a 0,972 (otra) | 0,98 a 1,22 | 0,89 a 0,94 |
| Pluralidad | 0,958 a 0,971 | 1,04 a 1,20 | 0,89 a 1,00 |
| Cohorte 2022 / 2023 | 0,960 / 0,961 | 1,03 / 1,06 | 0,90 / 0,91 |

- **Ningún grupo tiene alerta de discriminación.** Los AUROC más bajos (raza "otra" 0,942; Medicaid 0,949; madres negras 0,954) siguen muy por encima del límite.
- **Calibración:** una sola alerta, en las madres con raza desconocida (O/E 1,45, unos 64.000 nacimientos): el modelo subestima su riesgo. Su IC 95% por bootstrap (1,20–1,73) alcanza el límite de 1,25, así que la alerta se reporta como no confirmada (imprecisa); todos los subgrupos tienen un límite inferior del AUROC de 0,93 o más (notebook 06). La falta del dato puede reflejar registros incompletos de partos con más riesgo; conviene revisarlo localmente antes de usar el modelo.
- **Proporción marcada:** se marca más a las madres negras (16,1%) que a las blancas (9,1%). Corresponde a su mayor mortalidad neonatal (4,4 frente a 2,3 por 1.000), con la misma calibración, así que no indica un sesgo del modelo sino una diferencia real de riesgo.

## 4. Qué impulsa el riesgo (descriptivo, no causal)

| Tipo de predictor | Contribución (SHAP) |
|---|---|
| Estado al nacer: Apgar a los 5 minutos (40,5%), peso al nacer (22,9%), edad gestacional (4,5%) | 68% |
| Relacionados con la atención prenatal o del parto | 13,5% |
| Otros (madre, historia obstétrica, anomalías congénitas, pluralidad) | 19% |

Entre los factores relacionados con la atención, los que más pesan son la cesárea (3,0%), el número de controles prenatales (2,6%), el IMC (1,3%), el inicio tardío del control prenatal (1,2%), la ganancia de peso (0,9%), WIC (0,9%), el nacimiento fuera del hospital (0,8%) y el tabaquismo en el embarazo (0,7%).

Dos lecturas para la estrategia de prevención:

- **A los 5 minutos de nacer, el riesgo ya está determinado en buena parte** por la prematurez, el peso y el estado del recién nacido. El modelo sirve para actuar rápido sobre ese riesgo, no para evitarlo.
- **La prevención que reduce ese riesgo ocurre antes del parto:** acceso temprano y suficiente al control prenatal, control del tabaquismo y del estado nutricional, y parto en un lugar con el nivel de atención adecuado. Estos factores aparecen asociados al riesgo, pero su contribución no es causal (la cesárea, por ejemplo, suele ser una respuesta a una complicación, no su causa).

## 5. Condiciones para implementarlo en una entidad de salud

1. **Validación y recalibración local.** El modelo se desarrolló con estadísticas vitales de EE. UU. Antes de usarlo en otro país, como Colombia, hay que validarlo con datos locales y recalibrar al menos el intercepto, porque la mortalidad neonatal de base es distinta.
2. **Datos disponibles a los 5 minutos.** Necesita los datos del certificado de nacimiento o de la historia clínica en ese momento: edad gestacional, peso, Apgar, pluralidad, anomalías, antecedentes y datos del embarazo y del parto.
3. **Umbral según capacidad.** El corte de 1% supone unas 19 valoraciones prioritarias por cada 1.000 nacimientos. Una entidad con menos capacidad puede usar el 1% de mayor riesgo (10 por 1.000, 75% de las muertes).
4. **Monitoreo.** Revisar cada año la calibración y el desempeño por subgrupos, en especial en los grupos con datos incompletos.

## 6. Limitaciones

- Datos administrativos de certificados: no hay variables clínicas detalladas (laboratorios, ecografía, monitoreo fetal).
- Sin geografía en los archivos públicos: no se puede evaluar el desempeño por región ni por nivel de atención del hospital.
- La contribución de los predictores es descriptiva; no permite afirmar que modificar un factor cambie el riesgo.
