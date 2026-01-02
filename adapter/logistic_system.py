import numpy as np
from adapter.base import SystemAdapter


class LogisticSystemAdapter(SystemAdapter):

    def __init__(self, x):
        self.x = x

    def fit_models(self, state):
        x_t = self.x[:-1]
        x_next = self.x[1:]
        denom = ((x_t * (1 - x_t)) ** 2).sum()
        r = (x_next * x_t * (1 - x_t)).sum() / denom
        state.representations["logistic"] = r

    def compute_error(self, state) -> float:
        r = state.representations["logistic"]
        preds = r * self.x[:-1] * (1 - self.x[:-1])
        return ((self.x[1:] - preds) ** 2).mean()

    def update_assumptions(self, state):
        pass
