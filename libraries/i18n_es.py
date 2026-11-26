# -*- coding: utf-8 -*-
"""Spanish labels for the outputs of the notebooks (used by libraries/i18n.py when LANG = "es").

Keys are the English labels. In a key, "#" stands for a number: "top #% of risk" matches "top 10% of risk", and the
numbers are put back in the same order in the translation. A range such as "2016-2021" or "0-27" counts as two numbers
("##"). NCHS field codes (MAGER, AB_NICU...), learner codes (LR, RF, ET, XGB), hyperparameter names and library names
are not translated. RULES holds labels built from a pattern; {0}, {1}... are the translated groups.
"""

ES = {
    # ---------------------------------------------------------------- general words and values
    "births": "nacimientos", "births (weighted)": "nacimientos (ponderados)", "events": "eventos",
    "deaths": "muertes", "records": "registros", "population": "población", "cohort": "cohorte",
    "cohorts": "cohortes", "value": "valor", "estimate": "estimación", "status": "estado", "rule": "regla",
    "item": "ítem", "content": "contenido", "field": "campo", "group": "grupo", "level": "nivel", "band": "banda",
    "flag": "alerta", "flagged": "alertados", "% flagged": "% alertados", "info": "información", "n": "n",
    "min": "mín.", "max": "máx.", "median": "mediana", "pct": "%", "missing": "faltante", "unknown": "desconocido",
    "other": "otro", "Other": "Otra", "yes": "sí", "ok": "ok", "fixed": "fijo", "passes": "cumple",
    "DOES NOT PASS": "NO CUMPLE", "PASSED": "CUMPLE", "NOT PASSED": "NO CUMPLE", "reproduced": "reproducido",
    "not applicable": "no aplica", "none": "ninguno", "—": "—", "minutes": "minutos", "# times": "# veces",
    "# vs #": "# vs #", "Selection": "Selección", "Data": "Datos", "Development data": "Datos de desarrollo",
    "learner": "algoritmo", "primary learner": "algoritmo principal", "primary learner (rule)": "algoritmo principal (regla)",
    "best base learner by AUROC": "mejor algoritmo base por AUROC", "best combination": "mejor combinación",
    "hyperparameters": "hiperparámetros", "ensemble adopted": "ensamble adoptado",
    "ensemble adopted in notebook #": "ensamble adoptado en el notebook #", "Stack": "Stack (ensamble)",
    "Stack - primary AUROC": "Stack - AUROC del algoritmo principal", "inner AUROC": "AUROC interno",
    "random seed": "semilla aleatoria", "data source": "fuente de datos", "data use": "uso de los datos",
    "raw files": "archivos originales", "publication rule": "regla de publicación", "python": "python",
    "PREDICTOR": "PREDICTOR", "EARLY IDENTIFIER": "IDENTIFICADOR TEMPRANO", "INSUFFICIENT SIGNAL": "SEÑAL INSUFICIENTE",
    "classification": "clasificación", "classification (framework #)": "clasificación (framework #)",
    "classification under framework #": "clasificación con el framework #",
    "classification under framework # (traceability)": "clasificación con el framework # (trazabilidad)",

    # ---------------------------------------------------------------- metrics
    "AUROC (#% CI)": "AUROC (IC #%)", "AUROC #%": "AUROC #%", "AUPRC #%": "AUPRC #%",
    "AUPRC (weighted)": "AUPRC (ponderada)", "AUROC SD across repeats": "DE del AUROC entre repeticiones",
    "Brier": "Brier", "ECE": "ECE", "accuracy": "exactitud", "F1": "F1", "sensitivity": "sensibilidad",
    "specificity": "especificidad", "PPV": "VPP", "NPV": "VPN", "TP": "VP", "FP": "FP", "TN": "VN", "FN": "FN",
    "calibration slope": "pendiente de calibración", "calibration slope #%": "pendiente de calibración #%",
    "calibration intercept": "intercepto de calibración", "calibration intercept #%": "intercepto de calibración #%",
    "observed/expected": "observado/esperado", "observed/expected #%": "observado/esperado #%", "O/E": "O/E",
    "prevalence": "prevalencia", "threshold": "umbral", "net benefit": "beneficio neto",
    "net benefit model": "beneficio neto del modelo", "net benefit treat all": "beneficio neto de tratar a todos",
    "risk cut": "corte de riesgo", "risk >= #%": "riesgo >= #%", "risk >= #% (recommended)": "riesgo >= #% (recomendado)",
    "top #%": "#% superior", "top #% of risk": "#% superior del riesgo", "Top #% of risk": "#% superior del riesgo",
    "operating point": "punto de operación", "deaths found per # births": "muertes encontradas por # nacimientos",
    "flagged per # births": "alertados por # nacimientos", "alerts per death found": "alertas por muerte encontrada",
    "events in top #% (%)": "eventos en el #% superior (%)", "events in top #% vs chance": "eventos en el #% superior vs azar",
    "sensitivity at top-#% cut": "sensibilidad con el corte del #% superior",
    "% flagged at top-#% cut": "% alertados con el corte del #% superior",
    "balanced point: risk cut": "punto equilibrado: corte de riesgo",
    "balanced point: sensitivity": "punto equilibrado: sensibilidad",
    "balanced point: specificity": "punto equilibrado: especificidad",
    "sensitivity when specificity >= #": "sensibilidad cuando la especificidad >= #",
    "specificity when sensitivity >= #": "especificidad cuando la sensibilidad >= #",
    "some threshold gives both >= #": "algún umbral da ambas >= #",
    "accuracy # · F1 # · sens. #": "exactitud # · F1 # · sens. #",
    "mean |SHAP| (log-odds)": "media |SHAP| (log-odds)", "share of total (%)": "parte del total (%)",

    # ---------------------------------------------------------------- figures
    "# - specificity (false positive rate)": "# - especificidad (tasa de falsos positivos)",
    "Sensitivity (true positive rate)": "Sensibilidad (tasa de verdaderos positivos)",
    "Predicted: event": "Predicho: evento", "Predicted: no event": "Predicho: sin evento",
    "Observed: event": "Observado: evento", "Observed: no event": "Observado: sin evento",
    "Preliminary run: comparison part (#% of development)": "Corrida preliminar: parte de comparación (#% del desarrollo)",
    "Internal validation ## (out-of-fold, repeat #)": "Validación interna ## (fuera de pliegue, repetición #)",
    "Temporal validation ##": "Validación temporal ##",
    "Sensitivity analyses: model fitted once, predictions restricted": "Análisis de sensibilidad: modelo ajustado una vez, predicciones restringidas",
    "Refitted sensitivity analyses": "Análisis de sensibilidad reajustados",
    "Internal ## top #% of risk": "Interna ## #% superior del riesgo",
    "Temporal ## top #% of risk": "Temporal ## #% superior del riesgo",
    "Recommended cut: risk >= #%": "Corte recomendado: riesgo >= #%",
    "Temporal test ## (model fitted once on ##)": "Prueba temporal ## (modelo ajustado una vez en ##)",
    "Temporal test ## (check: same model as the temporal validation of notebook #)": "Prueba temporal ## (verificación: el mismo modelo de la validación temporal del notebook #)",
    "Contribution of each predictor (top #; temporal test, weighted)": "Contribución de cada predictor (# principales; prueba temporal, ponderada)",
    "Share of the total contribution by type of predictor (%)": "Parte de la contribución total por tipo de predictor (%)",
    "LR · internal ##": "LR · interna ##", "LR · temporal ##": "LR · temporal ##",
    "XGB · internal ##": "XGB · interna ##", "XGB · temporal ##": "XGB · temporal ##",
    "reference (GA + birthweight)": "referencia (EG + peso al nacer)",
    "reference (GA + birthweight) · internal ##": "referencia (EG + peso al nacer) · interna ##",
    "reference (GA + birthweight) · temporal ##": "referencia (EG + peso al nacer) · temporal ##",
    "XGB native missing (diagnostic)": "XGB con faltantes nativos (diagnóstico)",

    # ---------------------------------------------------------------- notebook 01
    "Data adapter: birth cohorts built from the NCHS Period/Cohort Linked Birth/Infant Death public-use files (aggregate counts only)":
        "Adaptador de datos: cohortes de nacimientos construidas con los archivos de uso público NCHS Period/Cohort Linked Birth/Infant Death (solo conteos agregados)",
    "pop = live births to US-resident mothers with combined gestation ## weeks; main label = neonatal death at ## days":
        "pob = nacidos vivos de madres residentes en EE. UU. con gestación combinada de ## semanas; etiqueta principal = muerte neonatal a los ## días",
    "Linkage of infant deaths to their birth (the adapter stops below #%)": "Enlace de las muertes infantiles con su nacimiento (el adaptador se detiene por debajo del #%)",
    "births_us_resident": "nacimientos_residentes_EEUU", "infant_deaths_linked": "muertes_infantiles_enlazadas",
    "ga_unknown": "EG_desconocida", "ga_lt2#": "EG_menor_2#", "pop_ge2#wk": "pob_2#sem_o_más",
    "events_main_pop": "eventos_principal_pob", "events_first2#h_pop": "eventos_primeras_2#h_pob",
    "events_day1_2#_pop": "eventos_día1_2#_pob", "events_early_neonatal_pop": "eventos_neonatal_precoz_pob",
    "events_main_ge2#": "eventos_principal_2#sem_o_más",
    "infant deaths of the cohort (US residents)": "muertes infantiles de la cohorte (residentes en EE. UU.)",
    "joined to their birth": "enlazadas con su nacimiento", "% joined": "% enlazadas", "check (>= #%)": "verificación (>= #%)",
    "cohorts ##": "cohortes ##", "cohorts ## (pandemic)": "cohortes ## (pandemia)",
    "infant deaths joined to their birth (lowest cohort, %)": "muertes infantiles enlazadas con su nacimiento (cohorte más baja, %)",
    "population (US residents, ## weeks)": "población (residentes en EE. UU., ## semanas)",
    "neonatal deaths ## days": "muertes neonatales ## días", "deaths per # live births": "muertes por # nacidos vivos",
    "early neonatal deaths ## days": "muertes neonatales precoces ## días",
    "neonatal deaths at # weeks or more": "muertes neonatales a las # semanas o más",
    "NCHS (CDC) Period/Cohort Linked Birth/Infant Death public-use files, releases #/# to #/#":
        "Archivos de uso público NCHS (CDC) Period/Cohort Linked Birth/Infant Death, versiones #/# a #/#",
    "NCHS data use agreement: statistical analysis only; no re-identification; no linkage to identifiable data; data not redistributed":
        "Acuerdo de uso de datos del NCHS: solo análisis estadístico; sin reidentificación; sin enlace con datos identificables; los datos no se redistribuyen",
    "only aggregate outputs (data/outputs_*.txt); counts ## shown as <#; record-level files stay in data/ (not versioned)":
        "solo salidas agregadas (data/outputs_*.txt); conteos ## se muestran como <#; los archivos por registro quedan en data/ (no versionados)",
    "reference counts": "conteos de referencia",
    "written by this notebook (data/outputs_0#_build_cohorts.txt) and reproduced by notebook # (gate G1)":
        "escritos por este notebook (data/outputs_0#_build_cohorts.txt) y reproducidos por el notebook # (puerta G1)",
    "# of # ZIP files in /sessions/rcw-#nsbdbq5af5afirdfrjn1q8/mnt/Tesis/NCHS_data/raw": "# de # archivos ZIP en la carpeta de datos originales",

    # ---------------------------------------------------------------- notebook 02
    "Count audit of the neonatal population (aggregate counts only; ## shown as <#)":
        "Auditoría de conteos de la población neonatal (solo conteos agregados; ## se muestran como <#)",
    "Gate G1: reference counts reproduced": "Puerta G1: conteos de referencia reproducidos",
    "gate G1 (reference counts reproduced)": "puerta G1 (conteos de referencia reproducidos)",
    "Q-N1 Population (US residents, ## weeks) and events by label": "Q-N1 Población (residentes en EE. UU., ## semanas) y eventos por etiqueta",
    "Q-N2 Neonatal deaths by age at death (day # split into <# h and ## h)": "Q-N2 Muertes neonatales por edad al morir (día # dividido en <# h y ## h)",
    "Q-N2b Share of the neonatal deaths: day # day # days ## together and days ##": "Q-N2b Parte de las muertes neonatales: día # día # días ## juntos y días ##",
    "Q-N3 Gestational-age bands (combined gestation), cohorts ##": "Q-N3 Bandas de edad gestacional (gestación combinada), cohortes ##",
    "Q-N3b Gestational age and birthweight imputed by NCHS (% of the population)": "Q-N3b Edad gestacional y peso al nacer imputados por el NCHS (% de la población)",
    "Q-N5 Numeric candidates: % unknown and percentiles": "Q-N5 Candidatos numéricos: % desconocido y percentiles",
    "Q-N6 % unknown by cohort, whole population": "Q-N6 % desconocido por cohorte, población completa",
    "Q-N6b Candidates with more than #% unknown in any cohort": "Q-N6b Candidatos con más del #% desconocido en alguna cohorte",
    "Q-N7 Gate G2: AUROC of the number of unknown fields alone (neonatal death ## days)": "Q-N7 Puerta G2: AUROC del número de campos desconocidos solo (muerte neonatal ## días)",
    "Q-N7b Number of unknown fields: births (whole population)": "Q-N7b Número de campos desconocidos: nacimientos (población completa)",
    "AUROC of the number of unknowns": "AUROC del número de desconocidos",
    "AUROC of the number of unknowns alone": "AUROC del número de desconocidos solo",
    "population_ge2#": "población_2#sem_o_más", "events_0_2#d": "eventos_0_2#d", "early_0_6d": "precoz_0_6d",
    "events_ge2#": "eventos_2#sem_o_más", "post_neonatal_2#d_1y": "posneonatal_2#d_1a",
    "under_1h": "menos_1h", "first_2#h": "primeras_2#h", "day1_2#": "día1_2#", "day_1": "día_1", "day_2": "día_2",
    "day_3": "día_3", "day_4": "día_4", "day_5": "día_5", "day_6": "día_6", "day_7_2#": "días_7_2#",
    "day0_pct": "día0_%", "day1_pct": "día1_%", "day0_plus_day1_pct": "día0_más_día1_%", "day2_2#_pct": "días2_2#_%",
    "pct_population": "%_población", "pct_events": "%_eventos", "pct_unknown": "%_desconocido",
    "pct_not_applicable_8#": "%_no_aplica_8#", "per_1#": "por_1#", "ga_imputed_pct": "EG_imputada_%",
    "bw_imputed_pct": "peso_imputado_%", "all_cohorts": "todas_las_cohortes", "ge2#_weeks": "2#_semanas_o_más",
    "day-# deaths, first vs last cohort": "muertes del día #, primera vs última cohorte",
    "candidates with more than #% unknown in any cohort": "candidatos con más del #% desconocido en alguna cohorte",
    "% of births at ## weeks": "% de nacimientos a las ## semanas", "% of deaths at ## weeks": "% de muertes a las ## semanas",
    "## weeks": "## semanas", "# weeks or more": "# semanas o más",

    # ---------------------------------------------------------------- notebook 03
    "Predictor table and gates G2 and G3 of the neonatal model (aggregate output only)":
        "Tabla de predictores y puertas G2 y G3 del modelo neonatal (solo salida agregada)",
    "Gate G2: design checks": "Puerta G2: verificaciones de diseño",
    "no outcome, landmark, death-certificate or post-prediction field among the predictors":
        "ningún campo de desenlace, de landmark, del certificado de defunción ni posterior a la predicción entre los predictores",
    "no missingness or imputation indicator among the predictors (M4-D3)": "ningún indicador de faltante o de imputación entre los predictores (M4-D3)",
    "marital status excluded (M4-D2)": "estado civil excluido (M4-D2)",
    "unit of analysis is the live birth and the group is the unit itself (no mother identifier)":
        "la unidad de análisis es el nacido vivo y el grupo es la propia unidad (sin identificador de la madre)",
    "G2 leakage check: births by number of unknown predictor fields (development cohorts)":
        "Verificación de fuga G2: nacimientos por número de campos predictores desconocidos (cohortes de desarrollo)",
    "G2 leakage check: AUROC of the number of unknown fields alone (development cohorts)":
        "Verificación de fuga G2: AUROC del número de campos desconocidos solo (cohortes de desarrollo)",
    "Gate G3: data (development cohorts ##)": "Puerta G3: datos (cohortes de desarrollo ##)",
    "Gate G3: sample size (Riley et al.), planning and reassessment": "Puerta G3: tamaño de muestra (Riley et al.), planeación y reevaluación",
    "Primary learner rule (events per parameter >= #: best base learner of a preliminary run)":
        "Regla del algoritmo principal (eventos por parámetro >= #: mejor algoritmo base de una corrida preliminar)",
    "events per parameter = #": "eventos por parámetro = #",
    "development births": "nacimientos de desarrollo", "development events": "eventos de desarrollo",
    "Cox-Snell R2 max": "R2 de Cox-Snell máximo", "sample used (all events + #% of non-events)": "muestra usada (todos los eventos + #% de los no eventos)",
    "main model (all predictors)": "modelo principal (todos los predictores)",
    "reference model (gestational age + birthweight)": "modelo de referencia (edad gestacional + peso al nacer)",
    "candidate parameters": "parámetros candidatos", "events per parameter": "eventos por parámetro",
    "assumed R2 (#% of max)": "R2 supuesto (#% del máximo)",
    "planning: n required (shrinkage)": "planeación: n requerido (encogimiento)",
    "planning: n required (optimism)": "planeación: n requerido (optimismo)",
    "planning: n required (overall risk)": "planeación: n requerido (riesgo global)",
    "planning: n required": "planeación: n requerido", "planning: events required": "planeación: eventos requeridos",
    "planning: parameters supported": "planeación: parámetros soportados", "planning: gate G3": "planeación: puerta G3",
    "observed Cox-Snell R2 (cross-validated)": "R2 de Cox-Snell observado (validación cruzada)",
    "% of maximum": "% del máximo",
    "reassessment: n required (shrinkage)": "reevaluación: n requerido (encogimiento)",
    "reassessment: n required (optimism)": "reevaluación: n requerido (optimismo)",
    "reassessment: n required (overall risk)": "reevaluación: n requerido (riesgo global)",
    "reassessment: n required": "reevaluación: n requerido", "reassessment: events required": "reevaluación: eventos requeridos",
    "reassessment: parameters supported": "reevaluación: parámetros soportados", "reassessment: gate G3": "reevaluación: puerta G3",
    "pct_missing": "%_faltante", "mean_or_pct_yes": "media_o_%_sí", "n_unknown": "n_desconocidos",
    "births in the contract table": "nacimientos en la tabla de contrato", "parameters": "parámetros",
    "largest % missing (predictor)": "mayor % faltante (predictor)", "gate G2, design checks": "puerta G2, verificaciones de diseño",
    "AUROC of the number of unknowns (development)": "AUROC del número de desconocidos (desarrollo)",
    "development births / events": "nacimientos / eventos de desarrollo",
    "gate G3, planning (main / reference)": "puerta G3, planeación (principal / referencia)",
    "gate G3, reassessment (main / reference)": "puerta G3, reevaluación (principal / referencia)",
    "observed Cox-Snell R2 (main / reference)": "R2 de Cox-Snell observado (principal / referencia)",
    "group_id = unit_id": "group_id = unit_id", "unique unit_id": "unit_id único",
    "read for the predictors": "leídos para los predictores",
    "a field recorded after the prediction point is read": "se lee un campo registrado después del punto de predicción",

    # ---------------------------------------------------------------- notebook 04
    "Preliminary run of the base learners (neonatal model, development ##)": "Corrida preliminar de los algoritmos base (modelo neonatal, desarrollo ##)",
    "development births (##)": "nacimientos de desarrollo (##)", "sample: events + #% of non-events": "muestra: eventos + #% de los no eventos",
    "fit/tune part": "parte de ajuste/sintonización", "comparison part": "parte de comparación",
    "events in comparison part": "eventos en la parte de comparación",
    "Random search (# combinations per learner, # inner folds on #% of the fit part)":
        "Búsqueda aleatoria (# combinaciones por algoritmo, # pliegues internos en el #% de la parte de ajuste)",
    "Spread of the inner AUROC over the combinations tried (how much the search mattered)":
        "Dispersión del AUROC interno entre las combinaciones probadas (cuánto importó la búsqueda)",
    "Preliminary comparison on the #% part (prevalence #)": "Comparación preliminar en la parte del #% (prevalencia #)",
    "Confusion matrices and accuracy (weighted to the full population of the comparison part)":
        "Matrices de confusión y exactitud (ponderadas a la población completa de la parte de comparación)",
    "Reference: accuracy of flagging nobody (all predicted without event)": "Referencia: exactitud de no alertar a nadie (todos predichos sin evento)",
    "native-XGBoost diagnostic minus XGBoost (AUROC)": "diagnóstico XGBoost nativo menos XGBoost (AUROC)",

    # ---------------------------------------------------------------- notebook 05
    "Main evaluation of the neonatal model (birth + # minutes)": "Evaluación principal del modelo neonatal (nacimiento + # minutos)",
    "Primary learner (notebook #)": "Algoritmo principal (notebook #)",
    "sample rows": "filas de la muestra", "development ##": "desarrollo ##", "temporal test ##": "prueba temporal ##",
    "Internal validation: # x #-fold cross-validation, recalibrated (development ##)":
        "Validación interna: validación cruzada # x # pliegues, recalibrada (desarrollo ##)",
    "Full model minus reference model (GA + birthweight): AUROC difference, paired bootstrap #% CI":
        "Modelo completo menos modelo de referencia (EG + peso al nacer): diferencia de AUROC, IC #% por bootstrap pareado",
    "Temporal validation: development ## single test ##": "Validación temporal: desarrollo ## prueba única ##",
    "Criterion C1: #-hour landmark on the out-of-fold predictions of the primary learner (# deaths on days ##; # deaths on days ## removed)":
        "Criterio C1: landmark de # horas sobre las predicciones fuera de pliegue del algoritmo principal (# muertes en los días ##; # muertes en los días ## retiradas)",
    "AUROC full": "AUROC completo", "AUROC landmark": "AUROC landmark", "AUROC drop": "caída del AUROC",
    "AUPRC gain full": "ganancia AUPRC completa", "AUPRC gain landmark": "ganancia AUPRC landmark",
    "AUPRC gain kept (%)": "ganancia AUPRC conservada (%)",
    "Sensitivity analyses (primary learner, out-of-fold predictions of the model fitted once; observed/expected compares the deaths of each label with the predicted risk of death at ## days)":
        "Análisis de sensibilidad (algoritmo principal, predicciones fuera de pliegue del modelo ajustado una vez; observado/esperado compara las muertes de cada etiqueta con el riesgo predicho de muerte a los ## días)",
    "Refitted sensitivity analyses (primary learner): AUROC and events": "Análisis de sensibilidad reajustados (algoritmo principal): AUROC y eventos",
    "Gate G4: classification of the neonatal model (primary learner)": "Puerta G4: clasificación del modelo neonatal (algoritmo principal)",
    "Confusion matrix of the primary learner (out-of-fold, weighted to the development population)":
        "Matriz de confusión del algoritmo principal (fuera de pliegue, ponderada a la población de desarrollo)",
    "Decision curve (primary learner)": "Curva de decisión (algoritmo principal)",
    "Summary: discrimination, calibration and threshold metrics (top-#% cut)": "Resumen: discriminación, calibración y métricas con umbral (corte del #% superior)",
    "Summary: gate G4": "Resumen: puerta G4",
    "all births (main)": "todos los nacimientos (principal)", "all live births": "todos los nacidos vivos",
    "all live births (birth + # min)": "todos los nacidos vivos (nacimiento + # min)",
    "#-hour landmark (deaths on days ##)": "landmark de # horas (muertes en los días ##)",
    "#-hour landmark, refitted": "landmark de # horas, reajustado",
    "(a) + (c) #-hour landmark, # weeks or more": "(a) + (c) landmark de # horas, # semanas o más",
    "(b) early neonatal death ## days vs survivors (deaths on days ## removed)": "(b) muerte neonatal precoz ## días vs sobrevivientes (muertes en los días ## retiradas)",
    "(c) # weeks or more": "(c) # semanas o más", "# weeks or more, refitted": "# semanas o más, reajustado",
    "# weeks or more, reference model (GA + birthweight), refitted": "# semanas o más, modelo de referencia (EG + peso al nacer), reajustado",
    "early neonatal ## days": "neonatal precoz ## días",
    "complete records": "registros completos", "complete records (main model, no refit)": "registros completos (modelo principal, sin reajuste)",
    "complete records, refitted (no imputation)": "registros completos, reajustado (sin imputación)",
    "alive at the start of day #": "vivos al inicio del día #",
    "alive at the start of day # (deaths on days ##)": "vivos al inicio del día # (muertes en los días ##)",
    "C1 (#-hour landmark): AUROC drop": "C1 (landmark de # horas): caída del AUROC", "C1 met (framework #)": "C1 cumple (framework #)",
    "C2 met": "C2 cumple", "C3": "C3", "C4 met": "C4 cumple",
    "C1 events already present": "C1 eventos ya presentes", "C2 outcome with time": "C2 desenlace con tiempo",
    "C3 detection bias": "C3 sesgo de detección", "C4 stability over time": "C4 estabilidad en el tiempo",
    "met (AUROC #, #% CI ##; required >= # and >= #)": "cumple (AUROC #, IC #% ##; se requiere >= # y >= #)",
    "met (temporal AUROC #, #% CI ##; slope #, #% CI ##, required ##)": "cumple (AUROC temporal #, IC #% ##; pendiente #, IC #% ##, se requiere ##)",
    "met (#-hour landmark: AUROC drop #, #% CI ##, required <= #; AUPRC gain kept #%, #% CI ##%, reported, not decisive in framework #; framework # required >= #%: NOT met)":
        "cumple (landmark de # horas: caída del AUROC #, IC #% ##, se requiere <= #; ganancia AUPRC conservada #%, IC #% ##%, reportada, no decisiva en el framework #; el framework # exigía >= #%: NO cumple)",
    "not applicable (death certificate; linkage of deaths to births #%, notebook #)": "no aplica (certificado de defunción; enlace de muertes con nacimientos #%, notebook #)",

    # ---------------------------------------------------------------- notebook 06
    "Stage S1# (from classification to action) of the neonatal model, temporal test ##":
        "Etapa S1# (de la clasificación a la acción) del modelo neonatal, prueba temporal ##",
    "Workload at several operating points (temporal test ## weighted to the full population)":
        "Carga de trabajo en varios puntos de operación (prueba temporal ## ponderada a la población completa)",
    "Performance by subgroup (temporal test; whole-population AUROC #; flags: AUROC < # or O/E outside ##; gestational age descriptive only)":
        "Desempeño por subgrupo (prueba temporal; AUROC de la población completa #; alertas: AUROC < # u O/E fuera de ##; edad gestacional solo descriptiva)",
    "Original objective: best sensitivity-specificity pairs (temporal test ##)": "Objetivo original: mejores pares sensibilidad-especificidad (prueba temporal ##)",
    "Summary: operating points (temporal test ##)": "Resumen: puntos de operación (prueba temporal ##)",
    "Summary: model, equity and drivers": "Resumen: modelo, equidad y factores",
    "AUROC, temporal test": "AUROC, prueba temporal", "AUROC range across equity groups": "rango del AUROC entre grupos de equidad",
    "subgroups flagged": "subgrupos con alerta",
    "share of risk: gestational age and birthweight (%)": "parte del riesgo: edad gestacional y peso al nacer (%)",
    "share of risk: related to prenatal or delivery care (%)": "parte del riesgo: relacionada con la atención prenatal o del parto (%)",
    "gestational age and birthweight": "edad gestacional y peso al nacer",
    "related to prenatal or delivery care": "relacionado con la atención prenatal o del parto",
    "mother's race and Hispanic origin": "raza y origen hispano de la madre", "payment of the delivery": "pago del parto",
    "gestational age": "edad gestacional", "plurality": "pluralidad", "singleton": "único", "twin": "gemelar",
    "triplet or more": "triple o más", "private insurance": "seguro privado", "Medicaid": "Medicaid",
    "self-pay": "pago propio", "White": "Blanca", "Black": "Negra", "Hispanic": "Hispana", "Asian": "Asiática",
    "neonatal deaths": "muertes neonatales", "deaths per #": "muertes por #",

    # neonatal outcomes recorded after birth (E6 list of fields not read)
    "#-minute Apgar": "Apgar a los # minutos", "NICU admission": "ingreso a UCI neonatal",
    "antibiotics for the newborn": "antibióticos para el recién nacido", "assisted ventilation": "ventilación asistida",
    "ventilation > # hours": "ventilación > # horas", "seizures": "convulsiones", "surfactant": "surfactante",
    "breastfed at discharge": "lactancia materna al alta", "alive at report": "vivo al momento del reporte",
    "infant transferred": "recién nacido trasladado", "maternal transfusion": "transfusión materna",
    "perineal laceration": "laceración perineal", "ruptured uterus": "ruptura uterina", "hysterectomy": "histerectomía",
    "maternal ICU admission": "ingreso materno a UCI",

    # ---------------------------------------------------------------- predictors (contract table)
    "age": "edad", "race_black": "raza_negra", "race_hispanic": "raza_hispana", "race_asian": "raza_asiática",
    "race_other": "raza_otra", "educ_some_college": "educ_algo_de_universidad", "educ_bachelor_plus": "educ_pregrado_o_más",
    "born_outside_us": "nacida_fuera_EEUU", "pay_medicaid": "pago_medicaid", "pay_self": "pago_propio",
    "pay_other": "pago_otro", "wic": "wic", "prior_living_1": "hijos_vivos_previos_1",
    "prior_living_2plus": "hijos_vivos_previos_2_o_más", "prior_child_died": "hijo_previo_fallecido",
    "prior_other_termination": "otra_terminación_previa", "interval_lt18": "intervalo_menor_18",
    "interval_18_59": "intervalo_18_59", "interval_60plus": "intervalo_60_o_más", "interval_6#plus": "intervalo_6#_o_más",
    "prior_cesarean": "cesárea_previa", "prior_preterm_birth": "parto_pretérmino_previo",
    "care_after_first_trimester": "control_después_primer_trimestre", "no_prenatal_care": "sin_control_prenatal",
    "prenatal_visits": "controles_prenatales", "bmi": "imc", "weight_gain": "ganancia_de_peso",
    "smoked_during_pregnancy": "fumó_en_el_embarazo", "pregestational_diabetes": "diabetes_pregestacional",
    "gestational_diabetes": "diabetes_gestacional", "chronic_hypertension": "hipertensión_crónica",
    "gestational_hypertension": "hipertensión_gestacional", "eclampsia": "eclampsia",
    "infertility_treatment": "tratamiento_de_infertilidad", "gonorrhea": "gonorrea", "syphilis": "sífilis",
    "chlamydia": "clamidia", "hepatitis_b": "hepatitis_b", "hepatitis_c": "hepatitis_c", "induction": "inducción",
    "augmentation": "conducción", "antenatal_steroids": "corticoides_antenatales",
    "antibiotics_in_labor": "antibióticos_en_el_trabajo_de_parto", "chorioamnionitis": "corioamnionitis",
    "anesthesia": "anestesia", "presentation_breech": "presentación_podálica", "presentation_other": "presentación_otra",
    "delivery_forceps": "parto_fórceps", "delivery_vacuum": "parto_vacuum", "delivery_cesarean": "parto_cesárea",
    "trial_of_labor": "prueba_de_trabajo_de_parto", "born_out_of_hospital": "nacido_fuera_del_hospital",
    "attendant_midwife": "atendido_por_partera", "attendant_other": "atendido_por_otro",
    "triplet_or_more": "triple_o_más", "male": "masculino", "gestational_age": "edad_gestacional",
    "birthweight": "peso_al_nacer", "apgar5": "apgar5", "anencephaly": "anencefalia", "spina_bifida": "espina_bífida",
    "cyanotic_heart_disease": "cardiopatía_cianótica", "diaphragmatic_hernia": "hernia_diafragmática",
    "omphalocele": "onfalocele", "gastroschisis": "gastrosquisis", "limb_reduction": "reducción_de_extremidades",
    "cleft_lip": "labio_hendido", "cleft_palate": "paladar_hendido", "hypospadias": "hipospadias",
    "down_syndrome": "síndrome_de_down", "chromosomal_disorder": "trastorno_cromosómico",
    "age_missing": "edad_faltante",
}

# Labels built from a pattern ({0}, {1}...: the translated groups).
RULES = [
    (r"Q-N4 \[(\w+)\] (\w+): births and % of the population", "Q-N4 [{0}] {1}: nacimientos y % de la población"),
    (r"All combinations tried: (\w+)", "Todas las combinaciones probadas: {0}"),
    (r"(.+); (.+)", "{0}; {1}"),                    # readings joined with "; " (notebook 06)
    (r"(.+), (.+)", "{0}, {1}"),                    # lists ("group: level (O/E), group: level (O/E)")
    (r"(.+): (.+)", "{0}: {1}"),
    (r"(.+) \(O/E\)", "{0} (O/E)"),
]
ES.update({"mother": "madre", "obstetric_history": "historia_obstétrica", "current_pregnancy": "embarazo_actual",
           "labor_delivery": "trabajo_de_parto_y_parto", "newborn": "recién_nacido"})
ES.update({"# (# to #)": "# (# a #)", "# (# to +#)": "# (# a +#)", "+# (+# to +#)": "+# (+# a +#)",
           "# (notebooks # to #)": "# (notebooks # a #)"})

# Progress messages printed while the notebooks run (print)
ES.update({
    "cohort #: already built": "cohorte #: ya construida",
    "cohort #: # births written": "cohorte #: # nacimientos escritos",
    "repeat # done in # min": "repetición # terminada en # min",
    "# NCHS fields read for the predictors; none of the # fields recorded after birth + # minutes":
        "# campos del NCHS leídos para los predictores; ninguno de los # campos registrados después del nacimiento + # minutos",
    "Stack done in": "Stack terminado en", "done in": "terminado en", "done": "lista", "min": "min",
    "loaded from checkpoint": "cargado desde el checkpoint", "cohorts:": "cohortes:", "parameters:": "parámetros:",
    "primary learner:": "algoritmo principal:", "| written:": "| escrito:", "written:": "escrito:",
})

# Visible decisions of notebook 02
ES.update({
    "S4 decision: landmark of sensitivity analysis (a) (M4-D1)": "Decisión E4: punto de referencia del análisis de sensibilidad (a) (M4-D1)",
    "change in day-# deaths (%)": "cambio en las muertes del día # (%)",
    "change in deaths on days ## together (%)": "cambio en las muertes de los días ## juntos (%)",
    "day-# coding stable (change within #%)": "codificación del día # estable (cambio dentro de #%)",
    "decision": "decisión", "#-hour landmark kept": "se mantiene el punto de referencia a las # horas",
    "M4-D1: landmark moved to # hours (days ## together do not depend on how day # and day # are split)":
        "M4-D1: el punto de referencia pasa a las # horas (los días ## juntos no dependen de cómo se separen el día # y el día #)",
    "S4 decision: gestational age": "Decisión E4: edad gestacional",
    "consequence": "consecuencia",
    "sensitivity analysis (c) restricted to # weeks or more (outcome card)": "análisis de sensibilidad (c) restringido a # semanas o más (ficha del desenlace)",
    "gestational age imputed by NCHS, highest cohort (%)": "edad gestacional imputada por el NCHS, cohorte más alta (%)",
    "consequence for the imputed values": "consecuencia para los valores imputados",
    "kept as recorded; the imputation flags stay as metadata, not as predictors":
        "se usan como están registrados; las marcas de imputación quedan como metadatos, no como predictores",
    "S4 decision: candidates with more than #% unknown (M4-D2)": "Decisión E4: candidatos con más de #% de desconocidos (M4-D2)",
    "% unknown, all cohorts": "% desconocido, todas las cohortes",
    "% unknown, lowest-highest cohort": "% desconocido, cohorte más baja-más alta",
    "reporting change across cohorts": "cambio de reporte entre cohortes",
    "M4-D2: excluded": "M4-D2: excluido", "enters S7 (unknowns imputed)": "entra a E7 (desconocidos imputados)",
    "other candidates": "otros candidatos", "up to #": "hasta #", "enter S7": "entran a E7",
    "Preliminary G2 decision: handling of unknowns (M4-D3)": "Decisión previa de P2: manejo de los desconocidos (M4-D3)",
    "AUROC of the number of unknowns (population / # weeks or more)": "AUROC del número de desconocidos (población / # semanas o más)",
    "clearly above # (AUROC > #)": "claramente por encima de # (AUROC > #)",
    "M4-D3: imputation without missingness indicators, plus a complete-record sensitivity analysis":
        "M4-D3: imputación sin indicadores de faltante, más un análisis de sensibilidad con registros completos",
    "no special handling of unknowns": "sin tratamiento especial de los desconocidos",
    "S4 decision": "Decisión E4",
})
ES.update({
    "% of the deaths on day #, first vs last cohort": "% de las muertes en el día #, primera vs última cohorte",
    "% of the deaths on days ## together, first vs last cohort": "% de las muertes en los días ## juntos, primera vs última cohorte",
    "relative change of that share (%)": "cambio relativo de esa proporción (%)",
    "relative change of that share (%) ": "cambio relativo de esa proporción (%) ",
})
ES["% of the deaths on day # first vs last cohort"] = "% de las muertes en el día # primera vs última cohorte"   # "1," is read as one number

# Notebook 03: predictor table and visible decisions
ES.update({
    "#": "#", "parameter": "parámetro", "block": "bloque", "NCHS field": "campo NCHS", "type": "tipo",
    "reference model": "modelo de referencia", "continuous": "continuo",
    "binary (one level of the field)": "binario (un nivel del campo)",
    "obstetric history": "historia obstétrica", "current pregnancy": "embarazo actual",
    "labor and delivery": "trabajo de parto y parto", "newborn": "recién nacido",
    "# parameters from # NCHS fields (# continuous, # binary)": "# parámetros de # campos del NCHS (# continuos, # binarios)",
    "S5 decision: unit of analysis": "Decisión E5: unidad de análisis",
    "cohorts with one record per live birth": "cohortes con un registro por nacido vivo",
    "# of #": "# de #",
    "group = the birth itself in every cohort": "grupo = el propio nacimiento en todas las cohortes",
    "continue to S6 (no group can fall on both sides of a split)": "sigue a E6 (ningún grupo puede quedar a ambos lados de una partición)",
    "S6 decision: information window": "Decisión E6: ventana de información",
    "NCHS fields read for the predictors": "campos del NCHS leídos para los predictores",
    "fields recorded after birth + # minutes that are read": "campos registrados después del nacimiento + # minutos que se leen",
    "continue to S7 (only information known at birth + # minutes)": "sigue a E7 (solo información conocida al nacer + # minutos)",
    "S7 decision: missing values of the parameters": "Decisión E7: faltantes de los parámetros",
    "highest % missing": "mayor % faltante", "which": "cuáles", "all others": "todos los demás",
    "missing <= #%": "faltantes <= #%", "missing > #%": "faltantes > #%",
    "enter with median imputation, no missingness indicators (M4-D3)": "entran con imputación por la mediana, sin indicadores de faltante (M4-D3)",
    "enter: interpregnancy interval kept in the audit (S4, M4-D2 table); complete records as a sensitivity analysis":
        "entran: el intervalo entre embarazos se mantuvo en la auditoría (E4, tabla M4-D2); registros completos como análisis de sensibilidad",
    "G2 decision": "Decisión P2", "design checks passed": "verificaciones de diseño que pasan",
    "G2 passes; M4-D3 and the complete-record sensitivity analysis are kept; the native-XGBoost diagnostic is checked in notebook #":
        "P2 pasa; se mantienen M4-D3 y el análisis de sensibilidad con registros completos; el diagnóstico de XGBoost nativo se revisa en el notebook #",
    "G2 passes; no special handling of unknowns": "P2 pasa; sin tratamiento especial de los desconocidos",
    "G3 decision": "Decisión P3",
    "gate G3, planning and reassessment (main and reference)": "puerta P3, planeación y reevaluación (principal y referencia)",
    "events available / required (main model, reassessment)": "eventos disponibles / requeridos (modelo principal, reevaluación)",
    "G3 passes: preliminary run of the base learners (notebook #); with # or more events per parameter the primary learner is the best one of that run":
        "P3 pasa: corrida preliminar de los algoritmos base (notebook #); con # o más eventos por parámetro el algoritmo principal es el mejor de esa corrida",
    "G3 passes: preliminary run (notebook #)": "P3 pasa: corrida preliminar (notebook #)",
    "G3 not passed: feasibility and R1 to the next rung": "P3 no pasa: factibilidad y R1 al siguiente peldaño",
    "Gate G2: design checks": "Puerta P2: verificaciones de diseño",
})

# In Spanish the gates are P1-P4 and the stages E1-E11 (in English G1-G4 and S1-S11)
import re as _re
ES = {k: _re.sub(r"\bS(1[01]|[1-9])\b", r"E\1", _re.sub(r"\bG([1-4])\b", r"P\1", v)) for k, v in ES.items()}
ES.update({"binary (#/#)": "binario (#/#)"})

# Figures of notebooks 04 and 05: one ROC subplot per curve; classification report and confusion matrix
ES.update({
    "precision": "precisión", "recall": "sensibilidad (recall)", "f1-score": "F1", "accuracy": "exactitud",
    "macro avg": "promedio macro", "Metrics": "Métricas", "Classes": "Clases", "risk cut": "corte de riesgo",
    "Predicted label": "Clase predicha", "True label": "Clase real", "Confusion matrix": "Matriz de confusión",
})

# Notebook 05: final model saved (models/); notebook 06: 95% confidence intervals by subgroup (TRIPOD+AI)
ES.update({
    "Final model saved for reuse (models/)": "Modelo final guardado para reutilizarlo (models/)",
    "pipeline with Platt recalibration (joblib)": "pipeline con la recalibración de Platt (joblib)",
    "learner in portable format (XGBoost JSON)": "algoritmo en formato portable (XGBoost JSON)",
    "model card (predictors, imputation medians, Platt coefficients)": "ficha del modelo (predictores, medianas de imputación, coeficientes de Platt)",
    "check: max |difference|, reloaded joblib vs model in memory": "verificación: máx. |diferencia|, joblib recargado frente al modelo en memoria",
    "check: max |difference|, portable files vs model in memory": "verificación: máx. |diferencia|, archivos portables frente al modelo en memoria",
    "temporal AUROC with the reloaded model": "AUROC temporal con el modelo recargado",
    "not saved (the primary learner is not XGBoost)": "no se guarda (el algoritmo principal no es XGBoost)",
    "Performance by subgroup: #% confidence intervals (stratified bootstrap inside each subgroup, # resamples; temporal test ##)":
        "Desempeño por subgrupo: intervalos de confianza del #% (bootstrap estratificado dentro de cada subgrupo, # remuestreos; prueba temporal ##)",
    "reading": "lectura", "descriptive only": "solo descriptivo", "no flag": "sin alerta",
    "AUROC flag supported by the #% CI": "alerta de AUROC sostenida por el IC del #%",
    "AUROC flag not confirmed: the #% CI reaches the limit": "alerta de AUROC no confirmada: el IC del #% alcanza el límite",
    "O/E flag supported by the #% CI": "alerta de O/E sostenida por el IC del #%",
    "O/E flag not confirmed: the #% CI reaches the limit": "alerta de O/E no confirmada: el IC del #% alcanza el límite",
})
