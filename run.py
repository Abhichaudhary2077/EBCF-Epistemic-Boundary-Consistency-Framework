import numpy as np
import logging

from utils.logger import setup_logger
from utils.experiment import save_experiment_summary

from core.state import EpistemicState, Assumption
from core.consistency import ConsistencyMonitor
from core.identifiability import IdentifiabilityAnalyzer
from core.controller import EpistemicController

from adapter.toy_system import ToySystemAdapter
from reporting.reporting_text import generate_human_report


# -------------------------------
# Setup logging & experiment
# -------------------------------
log_file = setup_logger("toy_system")
logging.info("Starting EBCF Toy System Experiment")

# -------------------------------
# Generate data
# -------------------------------
np.random.seed(0)
y = np.cumsum(np.random.randn(100))

# -------------------------------
# Initialize epistemic state
# -------------------------------
state = EpistemicState(
    observables={"y": y},
    assumptions={
        "closed_system": Assumption(
            id="closed_system",
            description="System has no external inputs"
        )
    }
)

# -------------------------------
# Initialize adapter & controller
# -------------------------------
adapter = ToySystemAdapter(y)

controller = EpistemicController(
    ConsistencyMonitor(),
    IdentifiabilityAnalyzer()
)

# -------------------------------
# Main epistemic loop
# -------------------------------
for iteration in range(10):
    logging.info(f"Iteration {iteration + 1}")

    adapter.fit_models(state)
    error = adapter.compute_error(state)
    logging.info(f"Error: {error:.6f}")

    adapter.update_assumptions(state)

    boundary = controller.step(state, error)

    if boundary:
        logging.warning("Epistemic stop triggered")

        print("\nEPISTEMIC STOP CONFIRMED\n")
        generate_human_report(boundary, state)

        save_experiment_summary("toy_system", boundary, state)
        logging.info("Experiment summary saved")

        break

logging.info("Experiment finished")
