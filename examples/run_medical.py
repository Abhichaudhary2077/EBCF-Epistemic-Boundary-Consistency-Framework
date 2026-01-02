from core.state import EpistemicState, Assumption
from core.consistency import ConsistencyMonitor
from core.identifiability import IdentifiabilityAnalyzer
from core.controller import EpistemicController
from adapter.medical_system import MedicalSystemAdapter
from reporting.reporting_text import generate_human_report


symptoms = ["chest_pain"]
tests = {
    "ECG": "normal",
    "blood_test": None  # missing
}

state = EpistemicState(
    observables={
        "symptoms": symptoms,
        "tests": tests
    },
    assumptions={
        "sufficient_tests": Assumption(
            id="sufficient_tests",
            description="Available tests are enough to identify cause"
        )
    }
)

adapter = MedicalSystemAdapter(symptoms, tests)

controller = EpistemicController(
    ConsistencyMonitor(),
    IdentifiabilityAnalyzer()
)

for _ in range(5):
    adapter.fit_models(state)
    error = adapter.compute_error(state)
    adapter.update_assumptions(state)

    boundary = controller.step(state, error)

    if boundary:
        print("\nEPISTEMIC STOP CONFIRMED (MEDICAL CASE)\n")
        generate_human_report(boundary, state)
        break
