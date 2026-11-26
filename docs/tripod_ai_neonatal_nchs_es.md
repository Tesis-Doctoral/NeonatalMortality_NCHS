# Etapa E11 — lista TRIPOD+AI: modelo neonatal NCHS (M4)

Versión en inglés: [`tripod_ai_neonatal_nchs.md`](tripod_ai_neonatal_nchs.md). Lista de TRIPOD+AI (Collins et al., BMJ 2024;385:e078378), ítem por ítem, con **dónde** se reporta cada ítem para el modelo M4 (muerte neonatal de 0 a 27 días, archivos enlazados de nacimientos y muertes infantiles del NCHS, cohortes de nacimiento 2016–2023). Versión del 2026-11-25.

El estudio **desarrolla** el modelo (D: desarrollo 2016–2021, validación interna) y lo **evalúa** (E: prueba temporal 2022–2023, misma fuente). Los textos de los ítems están resumidos; la redacción exacta está en la lista oficial.

**Estado:** ✅ reportado en el repositorio · 📝 por escribir en la monografía o el artículo (el contenido existe) · ⚠️ brecha: hay que agregar algo · — no aplica (con la razón).

Abreviaturas: **FD** = ficha del desenlace [`outcome_card_neonatal_nchs_es.md`](outcome_card_neonatal_nchs_es.md); **NB0x** = `notebooks/0x_*_es.ipynb`; **OUT0x** = `data/outputs_0x_*.txt`; **E10** = [`e10_action_neonatal_es.md`](e10_action_neonatal_es.md); **FW** = framework ([StagedFramework_ClinicalPrediction](https://github.com/Tesis-Doctoral/StagedFramework_ClinicalPrediction)).

## Título y resumen

| Ítem | D/E | Contenido | Dónde | Estado |
|---|---|---|---|---|
| 1 | D;E | Desarrollo y evaluación de un modelo multivariable, población, desenlace | Título del capítulo de la monografía o del artículo: "desarrollo y validación temporal… muerte neonatal… nacidos vivos en Estados Unidos" | 📝 |
| 2 | D;E | Resumen según TRIPOD+AI para resúmenes | Monografía / artículo | 📝 |

## Introducción

| Ítem | D/E | Contenido | Dónde | Estado |
|---|---|---|---|---|
| 3a | D;E | Contexto en salud y justificación; modelos existentes | FD §1; literatura en la monografía (los modelos con edad gestacional, peso y Apgar suelen superar un AUROC de 0,85: FD §6) | 📝 |
| 3b | D;E | Población objetivo, lugar en la ruta de atención, usuarios | FD §1–§3 (nacidos vivos ≥ 22 semanas, 5 minutos después del nacimiento); E10 §1 (neonatología, priorización de la atención) | ✅ |
| 3c | D;E | Desigualdades en salud conocidas entre grupos | E10 §3 (mortalidad neonatal de 4,4 frente a 2,3 por 1.000 en madres negras y blancas); literatura en la monografía | 📝 |
| 4 | D;E | Objetivos: desarrollar, evaluar o ambos | FD §1; README (alcance) | ✅ |

## Métodos

| Ítem | D/E | Contenido | Dónde | Estado |
|---|---|---|---|---|
| 5a | D;E | Fuentes de datos de desarrollo y evaluación, representatividad | FD §2, §7; README (datos). Misma fuente para ambos: estadísticas vitales nacionales, todos los nacidos vivos de EE. UU. | ✅ |
| 5b | D;E | Fechas de los datos | FD §2, §7: cohortes de nacimiento 2016–2021 (desarrollo) y 2022–2023 (prueba); muertes hasta el primer año de vida | ✅ |
| 6a | D;E | Entorno, número y ubicación de los centros | FD §2, §7: toda la población de EE. UU., todos los estados; los archivos públicos no traen geografía ni hospital | ✅ |
| 6b | D;E | Criterios de elegibilidad | FD §2 (residentes en EE. UU., `COMBGEST` 22–47, edad gestacional desconocida excluida); NB02 (Q-N1, Q-N3) | ✅ |
| 6c | D;E | Tratamientos recibidos y cómo se manejaron | La atención anterior al punto de predicción entra como predictor (corticoides, antibióticos, inducción, vía del parto: FD §4); la posterior se excluye (FD §3; NB03 E6) | ✅ |
| 7 | D;E | Preparación de los datos y control de calidad, similitud entre grupos | `libraries/nchs_reader.py`; NB01 (enlace del 100%); NB02 (desconocidos por cohorte, decisiones M4-D1 y M4-D2); E10 §3 (raza desconocida) | ✅ |
| 8a | D;E | Desenlace, horizonte, cómo y cuándo se evaluó | FD §2: muerte de 0 a 27 días según el certificado de defunción enlazado; NB02 (edad al morir, M4-D1) | ✅ |
| 8b | D;E | Evaluación subjetiva del desenlace | — La muerte es objetiva (enlace de certificados) | — |
| 8c | D;E | Cegamiento de la evaluación del desenlace | — Los certificados de defunción se llenan sin el modelo; el enlace lo hace el NCHS automáticamente | — |
| 9a | D | Elección inicial de predictores y preselección | FD §4 (bloques fijados con la auditoría de conteos, nunca separados por desenlace); M4-D2 (estado civil excluido) | ✅ |
| 9b | D;E | Definición de cada predictor, cómo y cuándo se midió | NB03 (`make_predictors` y tabla de los 71 parámetros con su campo NCHS); FD §3 (nacimiento + 5 minutos) | ✅ |
| 9c | D;E | Evaluación subjetiva de predictores | El Apgar a los 5 minutos lo asigna quien atiende el parto; declararlo en la monografía | 📝 |
| 10 | D;E | Tamaño de muestra, desarrollo y evaluación | NB03 puerta P3 (Riley et al., dos pasos; 62.713 eventos frente a 104 requeridos); OUT03 | ✅ |
| 11 | D;E | Datos faltantes | M4-D3 (imputación por la mediana sin indicadores); NB03 E7 (% faltante por parámetro); NB05 (registros completos, con y sin reajuste) | ✅ |
| 12a | D | Uso de los datos: particiones, sin fuga | NB04 (partición 80/20), NB05 (validación cruzada 3 × 5, partición temporal por cohorte); NB03 puerta P2 (verificaciones de diseño) | ✅ |
| 12b | D | Manejo de los predictores (forma, escala, categorías) | NB03 (`make_predictors`: niveles de referencia, categorías agrupadas); escalamiento dentro del pipeline de la regresión logística | ✅ |
| 12c | D | Tipo de modelo, pasos de construcción, hiperparámetros, validación interna | NB04 (búsqueda aleatoria, 3 pliegues internos, ensamble, regla del algoritmo principal); NB05 (validación cruzada 3 × 5 con recalibración de Platt dentro del entrenamiento) | ✅ |
| 12d | D;E | Heterogeneidad entre grupos (clusters) | Los archivos no traen hospital ni geografía; heterogeneidad en el tiempo por cohorte (2020–2021 frente a 2016–2019, NB05; 2022 frente a 2023, NB06) | ✅ |
| 12e | D;E | Medidas de desempeño y comparación de modelos | NB05: AUROC, AUPRC, Brier, pendiente e intercepto de calibración, O/E, ECE, curva de decisión, exactitud y F1 en puntos de operación; bootstrap pareado frente al modelo de referencia | ✅ |
| 12f | E | Actualización del modelo tras la evaluación | Sin actualización en la prueba temporal: modelo ajustado una vez en 2016–2021 (la recalibración de Platt es parte del desarrollo) | ✅ |
| 12g | E | Cómo se calcularon las predicciones en la evaluación | Código de NB05/NB06; modelo final en `models/` y `libraries/neonatal_model.py` (predicciones reproducidas desde los archivos guardados, verificado en NB05) | ✅ |
| 13 | D;E | Métodos para el desbalance de clases | Muestra caso-control (todos los eventos + 2% de los no eventos) con pesos 1/0,02 y recalibración de Platt, para que probabilidades y métricas se refieran a toda la población (NB04, NB05) | ✅ |
| 14 | D;E | Enfoque de equidad | E10 §3 y NB06: subgrupos (raza y origen hispano, pago, pluralidad, cohorte) con alertas fijadas antes de correr | ✅ |
| 15 | D | Salida del modelo, umbrales y cómo se eligieron | Probabilidad de muerte de 0 a 27 días; puntos de operación en NB06 y E10 §2 (riesgo ≥ 1% recomendado por carga de trabajo) | ✅ |
| 16 | D;E | Diferencias entre los datos de desarrollo y de evaluación | Misma fuente, definiciones y predictores; solo cambian los años de las cohortes (FD §2). El cambio de codificación de las muertes del día 1 se maneja con M4-D1 | ✅ |
| 17 | D;E | Aprobación ética y consentimiento | [`ethics_statement_neonatal_es.md`](ethics_statement_neonatal_es.md): datos públicos y anonimizados bajo las condiciones de uso del NCHS; no es investigación con sujetos humanos (45 CFR 46.102); investigación sin riesgo (Resolución 8430 de 1993, art. 11); consentimiento no aplica. Falta solo el concepto del comité de ética de Uninorte (acta y fecha) | ✅ (falta el concepto del comité) |

## Ciencia abierta

| Ítem | D/E | Contenido | Dónde | Estado |
|---|---|---|---|---|
| 18a | D;E | Financiación | Monografía | 📝 |
| 18b | D;E | Conflictos de interés | Monografía | 📝 |
| 18c | D;E | Protocolo y desviaciones | FW (framework por etapas) + FD (decisiones fechadas); desviaciones registradas: M4-D1 a M4-D3, framework 1.3 ([`decision_G4_C1_2026-11-23_es.md`](decision_G4_C1_2026-11-23_es.md)) | ✅ |
| 18d | D;E | Registro | No registrado; declararlo | 📝 |
| 18e | D;E | Disponibilidad de los datos | Archivos públicos del NCHS, enlace de descarga y condiciones (FD §7, README); no se redistribuyen | ✅ |
| 18f | D;E | Disponibilidad del código, software y versiones | GitHub (Tesis-Doctoral/NeonatalMortality_NCHS), licencia MIT, `requirements.txt` con versiones exactas (Python 3.11.9) | ✅ |
| 19 | D;E | Participación de pacientes y público | No hubo; declararlo | 📝 |

## Resultados

| Ítem | D/E | Contenido | Dónde | Estado |
|---|---|---|---|---|
| 20a | D;E | Flujo de participantes, con y sin el desenlace | `figures/tripod_flow_es.png` (diagrama de flujo por período: nacimientos en los archivos, exclusiones, población analizada con sus muertes, muestra del modelo) y `data/outputs_tripod_flow_periods_es.txt`; `scripts/tripod_flow_and_periods.py` | ✅ |
| 20b | D;E | Características de los datos, predictores, faltantes | OUT03 (Q-P1: % faltante y media o % sí de los 71 parámetros); OUT02 | ✅ |
| 20c | E | Distribuciones de desarrollo frente a evaluación | `data/outputs_tripod_flow_periods_es.txt`: desenlace y 30 predictores principales en desarrollo frente a prueba temporal, con % desconocido y diferencia estandarizada; solo el tabaquismo en el embarazo difiere con |d| ≥ 0,10 (6,1% frente a 3,3%) | ✅ |
| 21 | D;E | Participantes y eventos en cada análisis | NB04 (partes de ajuste y de comparación), NB05 (muestras de desarrollo y temporal, eventos de cada sensibilidad), NB06 | ✅ |
| 22 | D | Especificación completa del modelo (fórmula, código, objeto) | Código e hiperparámetros (`data/outputs_04_selection.json`); modelo ajustado en `models/` (pipeline en joblib, XGBoost en JSON, ficha con el orden de los predictores, las medianas de imputación y los coeficientes de Platt) | ✅ |
| 23a | D;E | Desempeño con IC, subgrupos, gráficas | OUT05 (IC de cada métrica), figuras (ROC, matrices de confusión); subgrupos en NB06 con IC del 95% por bootstrap del AUROC y del O/E | ✅ |
| 23b | D;E | Heterogeneidad entre grupos | Por cohorte (NB05, NB06) | ✅ |
| 24 | E | Resultados de la actualización del modelo | — Sin actualización | — |

## Discusión y uso

| Ítem | D/E | Contenido | Dónde | Estado |
|---|---|---|---|---|
| 25 | D;E | Interpretación general, incluida la equidad | E10 §1–§4; FD §8 puntos 6–7 (lo que el modelo detecta: muertes en los dos primeros días); monografía | 📝 |
| 26 | D;E | Limitaciones | E10 §6; FD §2 (nacidos de un mismo parto no enlazados, ~1% de muertes sin enlazar) | ✅ |
| 27a | D | Datos de entrada de mala calidad o faltantes en el uso | E10 §5 (datos a los 5 minutos; riesgo subestimado con raza desconocida) | ✅ |
| 27b | D | Interacción y experticia de los usuarios | E10 §1, §5 (neonatología; umbral según la capacidad) | ✅ |
| 27c | D;E | Investigación futura | E10 §5 (validación y recalibración locales, por ejemplo en Colombia); monografía | 📝 |

## Brechas por cerrar antes del reporte

1. ✅ *Hecho (26/11/2026; NB05 corrido, los archivos recargados reproducen exactamente las predicciones).* **Modelo guardado (ítems 12g y 22).** El notebook 05 debería guardar el modelo principal ajustado (XGBoost en JSON y el calibrador de Platt) en `models/`, con un ejemplo corto de cómo predecir un nacimiento nuevo. Los datos no se pueden compartir, pero el modelo sí.
2. ✅ *Hecho (26/11/2026).* **Versiones fijas (18f).** `requirements.txt` lista los paquetes sin versión; agregar las versiones exactas usadas (Python, numpy, pandas, scikit-learn, xgboost) con `pip freeze` del entorno que corrió los notebooks.
3. ✅ *Hecho (26/11/2026): `scripts/tripod_flow_and_periods.py`.* **Diagrama de flujo y comparación de períodos (20a, 20c).** Una figura con el flujo desde todos los nacidos vivos hasta la población analizada, por período, y una tabla de los predictores principales y del desenlace en desarrollo frente a la prueba temporal.
4. ✅ *Declaración escrita (26/11/2026): `docs/ethics_statement_neonatal_es.md`; falta solo el concepto del comité de Uninorte.* **Ética (17).** Declaración de que el estudio usa datos públicos anonimizados; confirmar con Uninorte si se necesita una carta de exención del comité de ética.
5. ✅ *Hecho (26/11/2026; NB06 corrido).* **Intervalos de confianza por subgrupo (23a).** IC por bootstrap del AUROC y del O/E de cada subgrupo en NB06.

*Confidencial: uso interno del proyecto de investigación.*
