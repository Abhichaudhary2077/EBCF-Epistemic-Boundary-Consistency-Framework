import numpy as np
from adapter.base import SystemAdapter


class ToySystemAdapter(SystemAdapter):

    def __init__(self, y):
        self.y = y

    def fit_models(self, state):
        x = self.y[:-1]
        y_next = self.y[1:]
        a = (x @ y_next) / (x @ x)
        state.representations["linear"] = a

    def compute_error(self, state) -> float:
        a = state.representations["linear"]
        preds = a * self.y[:-1]
        error = ((self.y[1:] - preds) ** 2).mean()
        return error

    def update_assumptions(self, state):
        state.assumptions["closed_system"].status = "violated"
        state.assumptions["closed_system"].stress_score = 1.0
