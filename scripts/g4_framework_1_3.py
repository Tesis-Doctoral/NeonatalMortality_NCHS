"""Gate G4 under framework 1.3 (2026-11-23): criterion C1 is decided by the AUROC drop at the landmark only
(<= 0.05); the share of the AUPRC gain kept is still reported but no longer decides.

The change was adopted after seeing the result of notebook 05 (see docs/decision_G4_C1_2026-11-23.md).
This script does not refit anything: it reads the aggregate output of notebook 05, which already contains
every quantity C1 to C4 need, and restates the classification under framework 1.3 next to the one under 1.2.
Run from the repository root: python scripts/g4_framework_1_3.py
Writes data/outputs_05b_g4_framework_1_3.txt (aggregate only).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
txt = (ROOT / "data" / "outputs_05_main_evaluation.txt").read_text(encoding="utf-8")

def row(label):
    """Estimate, 2.5% and 97.5% of a row of the C1 table."""
    m = re.search(rf"^{re.escape(label)}\s+([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*$", txt, re.M)
    return tuple(float(v) for v in m.groups())

def g4(label):
    m = re.search(rf"^{re.escape(label)}\s+(.*)$", txt, re.M)
    return m.group(1).strip()

auroc_landmark, drop, gain = row("AUROC landmark"), row("AUROC drop"), row("AUPRC gain kept (%)")
c2_met = g4("C2 outcome with time").startswith("met")
c4_met = g4("C4 stability over time").startswith("met")
top10 = float(re.search(r"^events in top 10% vs chance\s+([\d.]+) times", txt, re.M).group(1))
internal_auroc = float(re.search(r"^AUROC\s+([\d.]+)\s+[\d.]+\s+[\d.]+\s*$", txt, re.M).group(1))   # first table: XGB

c1_v13 = drop[0] <= 0.05
c1_v12 = c1_v13 and gain[0] >= 100 * 2 / 3
def classify(c1):
    if internal_auroc >= 0.75 and c1 and c2_met and c4_met:
        return "PREDICTOR"
    return "EARLY IDENTIFIER" if internal_auroc >= 0.75 and top10 >= 2 else "NEITHER"

lines = [
    "Gate G4 of the neonatal model under framework 1.3 (aggregate output; source: data/outputs_05_main_evaluation.txt)",
    "",
    f"AUROC, whole population (internal validation)      {internal_auroc:.4f}",
    f"AUROC at the 48-hour landmark                      {auroc_landmark[0]:.4f} ({auroc_landmark[1]:.4f}-{auroc_landmark[2]:.4f})",
    f"AUROC drop (C1, decides in 1.3: <= 0.05)           {drop[0]:.4f} ({drop[1]:.4f}-{drop[2]:.4f})",
    f"AUPRC gain kept, % (reported; 1.2 required >= 67)  {gain[0]:.1f} ({gain[1]:.1f}-{gain[2]:.1f})",
    f"C1 framework 1.3                                   {'met' if c1_v13 else 'NOT met'}",
    f"C1 framework 1.2                                   {'met' if c1_v12 else 'NOT met'}",
    f"C2                                                 {'met' if c2_met else 'NOT met'}",
    "C3                                                 not applicable",
    f"C4                                                 {'met' if c4_met else 'NOT met'}",
    f"events in top 10% vs chance                        {top10:.2f} times",
    f"classification, framework 1.3                      {classify(c1_v13)}",
    f"classification, framework 1.2 (traceability)       {classify(c1_v12)}",
]
out = "\n".join(lines) + "\n"
print(out)
(ROOT / "data" / "outputs_05b_g4_framework_1_3.txt").write_text(out, encoding="utf-8")
