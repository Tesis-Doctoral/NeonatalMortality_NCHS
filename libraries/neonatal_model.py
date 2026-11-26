# -*- coding: utf-8 -*-
"""Use of the final neonatal model saved by notebook 05 (folder models/).

The model is the primary learner fitted once on the development cohorts 2016-2021 with its Platt recalibration:
the model whose temporal validation on 2022-2023 is reported (criterion C4). It returns the probability of death
at 0-27 days for a live birth, with the predictors known at birth + 5 minutes (built as in notebook 03,
`make_predictors`). The probabilities refer to the whole population (the case-control sample was weighted).

Two ways to use it:

1. With the same library versions as requirements.txt (joblib file: pipeline with imputation + learner + Platt):

    from libraries.neonatal_model import load_model, predict_risk
    model = load_model("models/neonatal_final_model.joblib")
    risk = predict_risk(model, births)          # births: DataFrame with the predictor columns

2. Portable, with any recent XGBoost (no pickle): the learner in JSON and the card with the predictor order, the
   imputation medians and the Platt coefficients:

    from libraries.neonatal_model import predict_from_card
    risk = predict_from_card("models/neonatal_final_model_card.json", "models/neonatal_final_xgb.json", births)

Both give the same probabilities (notebook 05 checks it). Suggested operating point for a priority assessment:
risk >= 1% (docs/e10_action_neonatal.md).
"""
import json
from pathlib import Path

import numpy as np


def _logit(p):
    p = np.clip(p, 1e-7, 1 - 1e-7)              # same clipping as the notebooks
    return np.log(p / (1 - p))


def load_model(path):
    """Load the joblib bundle: {"pipeline", "platt", "predictors", "learner"}."""
    import joblib
    return joblib.load(path)


def predict_risk(model, births):
    """Probability of neonatal death (0-27 days) for each row of `births`."""
    p = model["pipeline"].predict_proba(births[model["predictors"]])[:, 1]
    return model["platt"].predict_proba(_logit(p).reshape(-1, 1))[:, 1]


def predict_from_card(card_path, learner_path, births):
    """Same probabilities from the portable files: median imputation, XGBoost (JSON) and Platt recalibration."""
    import xgboost as xgb
    card = json.loads(Path(card_path).read_text(encoding="utf-8"))
    cols = card["predictors"]
    X = births[cols].astype("float64").to_numpy(copy=True)
    med = np.array([card["imputation_medians"][c] for c in cols], dtype=float)
    rows, cols_nan = np.where(np.isnan(X))
    X[rows, cols_nan] = med[cols_nan]
    p = xgb.Booster(model_file=str(learner_path)).predict(xgb.DMatrix(X))
    a, b = card["platt"]["intercept"], card["platt"]["slope_on_logit"]
    return 1 / (1 + np.exp(-(a + b * _logit(p))))
