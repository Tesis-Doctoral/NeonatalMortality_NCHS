# -*- coding: utf-8 -*-
"""TRIPOD+AI items 20a and 20c of the neonatal model (M4): flow of live births from the NCHS files to the analysed
population and the model samples, by period (development 2016-2021, temporal test 2022-2023), and the distribution of
the outcome and the main predictors in each period.

Reads only what the notebooks already produced: the counts of data/outputs_01_build_cohorts.txt, the sample sizes of
data/outputs_05_main_evaluation.txt and the contract table data/contract/neonatal_nchs_v1/ (notebook 03). Writes
aggregates only: data/outputs_tripod_flow_periods.txt (+ _es) and figures/tripod_flow.png (+ _es). Run from the root
of the repository: python scripts/tripod_flow_and_periods.py
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "data" / "contract" / "neonatal_nchs_v1"
OUT = ROOT / "data" / "outputs_tripod_flow_periods.txt"
FIG = ROOT / "figures"
PERIODS = {"development 2016-2021": list(range(2016, 2022)), "temporal test 2022-2023": [2022, 2023]}

# ----------------------------------------------------------------------------- flow (item 20a)
txt01 = (ROOT / "data" / "outputs_01_build_cohorts.txt").read_text(encoding="utf-8").splitlines()
years = [int(v) for v in next(l for l in txt01 if l.startswith("cohort ")).split()[1:]]
row = lambda name: [int(v) for v in next(l for l in txt01 if l.split() and l.split()[0] == name).split()[1:]]
c01 = pd.DataFrame({k: row(k) for k in ["births", "births_us_resident", "ga_unknown", "ga_lt22", "pop_ge22wk",
                                         "events_main_pop"]}, index=years)
txt05 = (ROOT / "data" / "outputs_05_main_evaluation.txt").read_text(encoding="utf-8")
samp = {k: [int(x) for x in re.search(rf"^{re.escape(k)}\s+(\d+)\s+(\d+)\s+(\d+)\s*$", txt05, re.M).groups()]
        for k in PERIODS}

flow = {}
for name, ys in PERIODS.items():
    s = c01.loc[ys].sum()
    other = int(s["births_us_resident"] - s["ga_unknown"] - s["ga_lt22"] - s["pop_ge22wk"])
    assert other == 0, f"the flow does not add up ({other})"
    assert samp[name][0] == s["pop_ge22wk"] and samp[name][1] == s["events_main_pop"], "outputs_05 and outputs_01 differ"
    flow[name] = {"live births in the NCHS files": int(s["births"]),
                  "excluded: mother not a US resident": int(s["births"] - s["births_us_resident"]),
                  "excluded: gestational age unknown": int(s["ga_unknown"]),
                  "excluded: gestational age under 22 weeks": int(s["ga_lt22"]),
                  "analysed population (22 weeks or more)": int(s["pop_ge22wk"]),
                  "neonatal deaths (0-27 days)": int(s["events_main_pop"]),
                  "neonatal deaths per 1,000": f"{1000 * s['events_main_pop'] / s['pop_ge22wk']:.2f}",
                  "model sample: all deaths + 2% of the other births": samp[name][2]}
flow = pd.DataFrame(flow)

# ----------------------------------------------------------------------------- distributions (item 20c)
VARS = ["age", "race_black", "race_hispanic", "race_asian", "race_other", "educ_bachelor_plus", "born_outside_us",
        "pay_medicaid", "wic", "prior_cesarean", "prior_preterm_birth", "no_prenatal_care", "prenatal_visits", "bmi",
        "smoked_during_pregnancy", "pregestational_diabetes", "gestational_diabetes", "chronic_hypertension",
        "gestational_hypertension", "infertility_treatment", "antenatal_steroids", "induction", "delivery_cesarean",
        "born_out_of_hospital", "twin", "triplet_or_more", "male", "gestational_age", "birthweight", "apgar5"]
EXTRA = ["label_main", "ge28", "n_unknown"]
acc = {p: {} for p in PERIODS}
for p, ys in PERIODS.items():
    for y in ys:
        t = pq.read_table(CONTRACT / f"cohort_{y}.parquet", columns=VARS + EXTRA).to_pandas()
        t["any_unknown"] = (t["n_unknown"] > 0).astype("float32")
        for v in VARS + ["label_main", "ge28", "any_unknown"]:
            x = t[v].astype("float64").to_numpy(); ok = ~np.isnan(x)
            a = acc[p].setdefault(v, np.zeros(4))
            a += [len(x), ok.sum(), x[ok].sum(), (x[ok] ** 2).sum()]
BINARY = {v for v in VARS + ["label_main", "ge28", "any_unknown"]
          if v not in ("age", "prenatal_visits", "bmi", "gestational_age", "birthweight", "apgar5")}
rows = {}
for v in ["label_main", "ge28", "any_unknown"] + VARS:
    r = {}
    st = {}
    for p in PERIODS:
        n, k, s1, s2 = acc[p][v]
        m = s1 / k; sd = np.sqrt(max(s2 / k - m * m, 0))
        st[p] = (m, sd)
        r["measure"] = "per 1,000" if v == "label_main" else "%" if v in BINARY else "mean (SD)"
        r[p] = (f"{1000 * m:.2f}" if v == "label_main" else
                                                            f"{100 * m:.1f}" if v in BINARY else f"{m:.1f} ({sd:.1f})")
        r[f"{p}: % unknown"] = round(100 * (n - k) / n, 1)
    (m0, s0), (m1, s1_) = st.values()
    pooled = np.sqrt((s0 ** 2 + s1_ ** 2) / 2)
    r["standardized difference"] = round((m1 - m0) / pooled, 3) if pooled > 0 else 0.0
    rows[v] = r
dist = pd.DataFrame(rows).T
dist.index.name = "variable"
big = dist.index[dist["standardized difference"].abs() >= 0.10].tolist()

# ----------------------------------------------------------------------------- Spanish labels
ES = {"live births in the NCHS files": "nacidos vivos en los archivos del NCHS",
      "excluded: mother not a US resident": "excluidos: madre no residente en EE. UU.",
      "excluded: gestational age unknown": "excluidos: edad gestacional desconocida",
      "excluded: gestational age under 22 weeks": "excluidos: edad gestacional menor de 22 semanas",
      "analysed population (22 weeks or more)": "población analizada (22 semanas o más)",
      "neonatal deaths (0-27 days)": "muertes neonatales (0 a 27 días)",
      "neonatal deaths per 1,000": "muertes neonatales por 1.000",
      "model sample: all deaths + 2% of the other births": "muestra del modelo: todas las muertes + 2% de los demás nacimientos",
      "development 2016-2021": "desarrollo 2016-2021", "temporal test 2022-2023": "prueba temporal 2022-2023",
      "label_main": "muerte neonatal (0-27 días)", "ge28": "28 semanas o más", "any_unknown": "algún predictor desconocido",
      "standardized difference": "diferencia estandarizada", "variable": "variable", "per 1,000": "por 1.000",
      "% unknown": "% desconocido", "mean (SD)": "media (DE)", "measure": "medida"}
def es(s):
    s = str(s)
    for k in sorted(ES, key=len, reverse=True):
        s = s.replace(k, ES[k])
    return s
def to_es(df):
    d = df.copy(); d.index = [es(i) for i in d.index]; d.columns = [es(c) for c in d.columns]
    return d.map(lambda v: es(v) if isinstance(v, str) else v)

note_en = ("Standardized difference = (temporal - development) / pooled SD, on the known values; |d| >= 0.10 is the usual "
           "threshold of a relevant difference. Variables with |d| >= 0.10: " + (", ".join(big) or "none") + ".")
note_es = ("Diferencia estandarizada = (temporal - desarrollo) / DE combinada, con los valores conocidos; |d| >= 0,10 es el "
           "umbral usual de una diferencia relevante. Variables con |d| >= 0,10: " + (", ".join(big) or "ninguna") + ".")
with pd.option_context("display.width", 250, "display.max_columns", 20, "display.max_colwidth", 80):
    OUT.write_text("TRIPOD+AI items 20a and 20c: flow of live births and development vs temporal-test distributions "
                   "(aggregates only)\n\n== Flow of live births by period (item 20a)\n" + flow.to_string() +
                   "\n\n== Outcome and main predictors by period (item 20c; whole population, no sampling)\n" +
                   dist.to_string() + "\n" + note_en + "\n", encoding="utf-8")
    OUT.with_name(OUT.stem + "_es.txt").write_text(
        "Ítems 20a y 20c de TRIPOD+AI: flujo de los nacidos vivos y distribuciones de desarrollo frente a la prueba "
        "temporal (solo agregados)\n\n== Flujo de los nacidos vivos por período (ítem 20a)\n" + to_es(flow).to_string() +
        "\n\n== Desenlace y predictores principales por período (ítem 20c; toda la población, sin muestreo)\n" +
        to_es(dist).to_string() + "\n" + note_es + "\n", encoding="utf-8")

# ----------------------------------------------------------------------------- figure (flow diagram)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def fmt(n, lang):
    s = f"{n:,}"
    return s.replace(",", ".") if lang == "es" else s

def draw(lang):
    import textwrap
    L = {"en": {"births": "Live births in the NCHS files", "excl": "Excluded", "nonres": "mother not a US resident",
                "gaunk": "gestational age unknown", "lt22": "under 22 weeks", "pop": "Analysed population (22 weeks or more)",
                "deaths": "neonatal deaths (0-27 days)", "per": "per 1,000", "sample": "Model sample",
                "rows": "rows: all deaths + 2% of the other births, weighted to the population",
                "use": ["Development: hyperparameter search (notebook 04), 3 × 5 cross-validation and final fit (notebook 05)",
                        "Temporal test: a single evaluation of the model fitted on 2016–2021 (notebooks 05 and 06)"],
                "title": "Flow of live births by period — neonatal model NCHS (M4)"},
         "es": {"births": "Nacidos vivos en los archivos del NCHS", "excl": "Excluidos", "nonres": "madre no residente en EE. UU.",
                "gaunk": "edad gestacional desconocida", "lt22": "menos de 22 semanas", "pop": "Población analizada (22 semanas o más)",
                "deaths": "muertes neonatales (0 a 27 días)", "per": "por 1.000", "sample": "Muestra del modelo",
                "rows": "filas: todas las muertes + 2% de los demás nacimientos, ponderadas a la población",
                "use": ["Desarrollo: búsqueda de hiperparámetros (notebook 04), validación cruzada 3 × 5 y ajuste final (notebook 05)",
                        "Prueba temporal: una sola evaluación del modelo ajustado con 2016–2021 (notebooks 05 y 06)"],
                "title": "Flujo de los nacidos vivos por período — modelo neonatal NCHS (M4)"}}[lang]
    W = lambda t, n=44: "\n".join(textwrap.wrap(t, n))
    fig, ax = plt.subplots(figsize=(13, 8.2)); ax.set_xlim(0, 13); ax.set_ylim(1.3, 10.4); ax.axis("off")
    def box(x, y, w, h, text, fc, ha="center"):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                    fc=fc, ec="#4A5A6A", lw=1.1))
        ax.text(x if ha == "center" else x - w / 2 + 0.2, y, text, ha=ha, va="center", fontsize=9.5, linespacing=1.35)
    arr = dict(arrowstyle="-|>", color="#4A5A6A", lw=1.1)
    for k, (p, col) in enumerate(zip(PERIODS, ["#DCE8F5", "#F5E6D3"])):
        f = flow[p]; x = 3.25 + 6.5 * k; xl = x - 1.9
        ax.text(x, 10.05, (["Desarrollo 2016–2021", "Prueba temporal 2022–2023"] if lang == "es" else
                           ["Development 2016–2021", "Temporal test 2022–2023"])[k], ha="center", fontsize=12.5, weight="bold")
        box(x, 9.1, 5.4, 0.9, f"{L['births']}\n{fmt(f.iloc[0], lang)}", col)
        ax.annotate("", xy=(xl, 5.55), xytext=(xl, 8.65), arrowprops=arr)
        box(x + 0.85, 7.1, 3.9, 1.55, f"{L['excl']}\n• {L['nonres']}: {fmt(f.iloc[1], lang)}\n• {L['gaunk']}: {fmt(f.iloc[2], lang)}"
                                     f"\n• {L['lt22']}: {fmt(f.iloc[3], lang)}", "#F2F2F2", ha="left")
        ax.annotate("", xy=(x - 1.1, 7.1), xytext=(xl, 7.1), arrowprops=arr)
        rate = f.iloc[6].replace(".", ",") if lang == "es" else f.iloc[6]
        box(x, 5.0, 5.4, 1.1, f"{L['pop']}\n{fmt(f.iloc[4], lang)}\n{L['deaths']}: {fmt(f.iloc[5], lang)} ({rate} {L['per']})", col)
        ax.annotate("", xy=(x, 3.75), xytext=(x, 4.45), arrowprops=arr)
        box(x, 3.15, 5.4, 1.2, f"{L['sample']}\n{fmt(f.iloc[7], lang)} {W(L['rows'], 50)}", col)
        ax.text(x, 2.2, W(L["use"][k], 62), ha="center", va="top", fontsize=9, color="#333333")
    ax.set_title(L["title"], fontsize=13.5, pad=4)
    FIG.mkdir(exist_ok=True)
    fig.savefig(FIG / ("tripod_flow_es.png" if lang == "es" else "tripod_flow.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

draw("en"); draw("es")
print(flow.to_string()); print(); print(dist.to_string()); print(note_en)
