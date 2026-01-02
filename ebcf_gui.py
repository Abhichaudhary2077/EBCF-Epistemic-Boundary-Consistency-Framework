import tkinter as tk
from tkinter import messagebox
from ebcf import epistemic_check


def run_check():
    observables = obs_entry.get().strip().split(",")
    missing = miss_entry.get().strip().split(",")

    observables = [o.strip() for o in observables if o.strip()]
    missing = [m.strip() for m in missing if m.strip()]

    result = epistemic_check(
        observables=observables,
        missing=missing
    )

    if result.allowed:
        messagebox.showinfo(
            "EBCF Result",
            f"Allowed to proceed.\nConfidence: {result.confidence:.2f}"
        )
    else:
        messagebox.showwarning(
            "EBCF Result",
            f"STOP — Answering would require guessing.\n\n"
            f"Reason: {result.reason}\n"
            f"Confidence: {result.confidence:.2f}"
        )


root = tk.Tk()
root.title("EBCF — Honest Reasoning Checker")

tk.Label(root, text="What do you KNOW? (comma separated)").pack()
obs_entry = tk.Entry(root, width=60)
obs_entry.pack(pady=5)

tk.Label(root, text="What do you NOT know? (comma separated)").pack()
miss_entry = tk.Entry(root, width=60)
miss_entry.pack(pady=5)

tk.Button(root, text="Check honesty", command=run_check).pack(pady=15)

root.mainloop()
