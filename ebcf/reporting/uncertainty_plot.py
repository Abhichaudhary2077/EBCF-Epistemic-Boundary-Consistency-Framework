import matplotlib.pyplot as plt
from pathlib import Path
import os
import time 


def plot_uncertainty(error_history, decision=None, autoshow=True):
    """
    Save and optionally open uncertainty evolution plot.
    """

    if not error_history:
        error_history = [0.0]

    Path("logs").mkdir(exist_ok=True)

    timestamp = int(time.time())
    filename = f"logs/uncertainty_{timestamp}.png"

    plt.figure(figsize=(8, 4))
    plt.plot(
        range(1, len(error_history) + 1),
        error_history,
        marker="o",
        linewidth=2
    )

    plt.xlabel("Iteration")
    plt.ylabel("Uncertainty")
    plt.title("EBCF — Uncertainty Evolution")

    if decision:
        plt.axhline(
            y=error_history[-1],
            linestyle="--",
            alpha=0.6,
            label=f"Decision: {decision}"
        )
        plt.legend()

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    print(f"[EBCF] Uncertainty plot saved → {filename}")

    if autoshow:
        try:
            os.startfile(filename)  # Windows
        except Exception:
            pass
