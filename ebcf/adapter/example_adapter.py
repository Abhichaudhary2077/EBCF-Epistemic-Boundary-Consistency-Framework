# 🧩 ADAPTER TEMPLATE (COPY-PASTE FILE)

'''📄 **`ebcf/adapter/example_adapter.py`**

```python'''
from ebcf.adapter.base import SystemAdapter


class ExampleAdapter(SystemAdapter):
    """
    Minimal adapter template for EBCF.

    This adapter does NOT solve the problem.
    It only tells EBCF whether uncertainty is reducible.
    """

    def __init__(self, observables):
        self.observables = observables

    def fit_models(self, state):
        """
        Attempt to explain the system.
        You can register representations here.
        """
        state.representations["example"] = "attempted"

    def compute_error(self, state) -> float:
        """
        Return a number representing uncertainty.

        Rules:
        - Lower = better understanding
        - Same value repeatedly = stagnation
        """
        if "required_info" not in self.observables:
            return 1.0  # cannot improve
        return 0.0     # uncertainty reducible

    def update_assumptions(self, state):
        """
        Stress or validate assumptions based on observables.
        """
        if "required_info" not in self.observables:
            if "required_info" in state.assumptions:
                state.assumptions["required_info"].status = "violated"
