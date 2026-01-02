import logging
from datetime import datetime


def setup_logger(experiment_name="ebcf_experiment"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/{experiment_name}_{timestamp}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )

    logging.info("Logger initialized")
    return log_filename
