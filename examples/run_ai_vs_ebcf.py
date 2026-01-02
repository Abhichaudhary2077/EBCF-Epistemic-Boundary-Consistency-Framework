from core.state import EpistemicState, Assumption
from core.consistency import ConsistencyMonitor
from core.identifiability import IdentifiabilityAnalyzer
from core.controller import EpistemicController

from adapter.medical_system import MedicalSystemAdapter
from reporting.reporting_text import generate_human_report
from ai.proposer import AIProposer
from core.veto import epistemic_veto


# -------------------------------
# Setup scenario
# -------------------------------
symptoms = ["chest_pain"]
tests = {
    "ECG": "normal",
    "blood_test": None
}

state = EpistemicState(
    observables={"symptoms": symptoms, "tests": tests},
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

ai = AIProposer()

boundary = None
MAX_ITER = 5

# -------------------------------
# Epistemic loop
# -------------------------------
for i in range(MAX_ITER):
    adapter.fit_models(state)
    error = adapter.compute_error(state)
    adapter.update_assumptions(state)

    candidate = controller.step(state, error)

    # Only accept stop AFTER minimum effort is satisfied
    if candidate is not None:
        boundary = candidate
        break

# -------------------------------
# AI vs EBCF comparison
# -------------------------------
print("\n--- AI PROPOSAL ---")
proposal = ai.propose(state)
print(proposal)

print("\n--- EBCF DECISION ---")
decision = epistemic_veto(boundary, proposal)
print(decision)

if boundary:
    print("\n--- EBCF REPORT ---")
    generate_human_report(boundary, state)
