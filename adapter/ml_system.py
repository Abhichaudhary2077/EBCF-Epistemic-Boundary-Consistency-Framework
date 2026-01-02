from adapter.base import SystemAdapter


class MLSystemAdapter(SystemAdapter):
    def __init__(self, losses):
        self.losses = losses

    def fit_models(self, state):
        # Attempt simple explanation
        state.representations["trend"] = "loss decreasing"

    def compute_error(self, state) -> float:
        # Error = instability in loss
        diffs = [
            abs(self.losses[i+1] - self.losses[i])
            for i in range(len(self.losses) - 1)
        ]
        return sum(diffs) / len(diffs)

    def update_assumptions(self, state):
        if max(self.losses) - min(self.losses) > 1.0:
            state.assumptions["stable_training"].status = "violated"
