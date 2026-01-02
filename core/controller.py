from core.boundary import BoundaryRecord


class EpistemicController:
    def __init__(self, consistency_monitor, identifiability_analyzer):
        self.consistency_monitor = consistency_monitor
        self.identifiability_analyzer = identifiability_analyzer
        self.error_history = []

    def step(self, state, error_value):
        # Track uncertainty evolution
        self.error_history.append(error_value)
        state.error_history.append(error_value)

        # Evaluate consistency trend
        state.consistency_status = self.consistency_monitor.evaluate(
            self.error_history
        )

        # Check identifiability (conservative by default)
        identifiable = self.identifiability_analyzer.check(state)

        # -----------------------------
        # Minimum epistemic effort rule
        # -----------------------------
        # Do not stop too early; require sufficient attempts
        if len(self.error_history) < 3:
            return None

        # -----------------------------
        # Epistemic stopping condition
        # -----------------------------
        if state.consistency_status != "improving" and not identifiable:
            return self._stop(state)

        return None

    def _stop(self, state):
        # Identify stressed or violated assumptions
        stressed = [
            a.id for a in state.assumptions.values()
            if a.status != "holding"
        ]

        # -----------------------------
        # Confidence calibration
        # -----------------------------
        iterations = len(self.error_history)

        if iterations < 3:
            confidence = 0.3
        else:
            recent_errors = self.error_history[-3:]
            variance = max(recent_errors) - min(recent_errors)
            confidence = 0.6 + (iterations / 10) - variance

        # Clamp confidence to sane bounds
        confidence = max(0.1, min(confidence, 1.0))

        return BoundaryRecord(
            structural_location="Dynamics ↔ Assumptions",
            assumption_context=stressed,
            representation_agreement="All representations failed consistently",
            epistemic_status="Non-identifiable under current observables",
            confidence=confidence
        )
