class IdentifiabilityAnalyzer:
    """
    Determines whether the current epistemic task is identifiable
    given the provided observables.
    """

    def check(self, state):
        # Explicit override: task-level declaration
        if hasattr(state, "identifiable"):
            return bool(state.identifiable)

        # Conservative default
        return False
