from core.state import EpistemicState, Assumption
from core.consistency import ConsistencyMonitor
from core.identifiability import IdentifiabilityAnalyzer
from core.controller import EpistemicController
from adapter.ml_system import MLSystemAdapter
from reporting.reporting_text import generate_human_report


losses = [0.9, 0.7, 1.2, 0.8, 1.3]

state = EpistemicState(
    observables={"losses": losses},
    assumptions={
        "stable_training": Assumption(
            id="stable_training",
            description="Training process is stable"
        )
    }
)

adapter = MLSystemAdapter(losses)

controller = EpistemicController(
    ConsistencyMonitor(),
    IdentifiabilityAnalyzer()
)

for _ in range(10):
    adapter.fit_models(state)
    error = adapter.compute_error(state)
    adapter.update_assumptions(state)

    boundary = controller.step(state, error)
    if boundary:
        generate_human_report(boundary, state)
        break
