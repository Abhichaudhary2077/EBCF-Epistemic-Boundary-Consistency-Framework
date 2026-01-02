from adapter.base import SystemAdapter


class MedicalSystemAdapter(SystemAdapter):
    """
    Simplified medical-style adapter.
    This does NOT diagnose.
    It only demonstrates epistemic limits.
    """

    def __init__(self, symptoms, tests):
        self.symptoms = symptoms
        self.tests = tests

    def fit_models(self, state):
        """
        Attempt simple rule-based explanations.
        """
        explanations = {
            "muscle_pain": 0,
            "acid_reflux": 0,
            "cardiac_issue": 0
        }

        if "chest_pain" in self.symptoms:
            explanations["muscle_pain"] += 1
            explanations["acid_reflux"] += 1
            explanations["cardiac_issue"] += 1

        if self.tests.get("ECG") == "normal":
            explanations["cardiac_issue"] -= 0.5

        state.representations["diagnostic_scores"] = explanations

    def compute_error(self, state) -> float:
        """
        Error = inability to separate explanations.
        Smaller difference → higher error.
        """
        scores = state.representations["diagnostic_scores"].values()
        spread = max(scores) - min(scores)
        return 1.0 - spread

    def update_assumptions(self, state):
        """
        Stress assumptions when tests are insufficient.
        """
        if not self.tests.get("blood_test"):
            state.assumptions["sufficient_tests"].status = "violated"
            state.assumptions["sufficient_tests"].stress_score = 1.0
