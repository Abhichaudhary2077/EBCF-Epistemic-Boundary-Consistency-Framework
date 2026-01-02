import numpy as np


class ConsistencyMonitor:
    def evaluate(self, error_history: list) -> str:
        if len(error_history) < 3:
            return "improving"

        slope = np.polyfit(range(len(error_history)), error_history, 1)[0]

        if abs(slope) < 1e-4:
            return "stagnant"

        if slope > 0:
            return "inconsistent"

        return "improving"
