from ebcf.flows.chest_pain import CHEST_PAIN_FLOW
from ebcf import epistemic_check
from ebcf.reporting.uncertainty_plot import plot_uncertainty


def ask_choice(question):
    options = question["options"]
    prompt = f'{question["text"]}\n[{ " / ".join(options) }]: '

    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print("Invalid input. Please choose one of:", options)


def ask_multi_choice(question):
    options = question["options"]
    prompt = (
        f'{question["text"]}\n'
        f'Options: {", ".join(options)}\n'
        "Enter comma-separated values: "
    )

    while True:
        raw = input(prompt).strip().lower()
        selections = [x.strip() for x in raw.split(",") if x.strip()]
        if selections and all(x in options for x in selections):
            return selections
        print("Invalid input. Allowed options:", options)


def run_flow(flow):
    print("\n=== EBCF — Epistemic Boundary Checker ===\n")
    print("Reference flow:", flow["presentation"].replace("_", " ").title())
    print("(Non-diagnostic, epistemic evaluation only)\n")

    observables = {}
    hard_stop = False

    for stage in flow["stages"]:
        for q in stage["questions"]:
            answer = (
                ask_choice(q)
                if q["type"] == "choice"
                else ask_multi_choice(q)
            )

            observables[q["id"]] = answer

            if q.get("hard_stop") and "none" not in answer:
                hard_stop = True
                break
        if hard_stop:
            break

    print("\n--- EBCF VERDICT ---\n")

    if hard_stop:
        print("🔴 SAFETY STOP")
        print("Red-flag indicators detected.")
        print("Seek urgent medical care.")

        plot_uncertainty([1.0], decision="SAFETY STOP")
        return

    result = epistemic_check(
        observables=observables,
        missing=["clinical_tests"]
    )

    if result.allowed:
        print("🟢 Reasoning allowed.")
        plot_uncertainty(result.error_history, decision="ALLOW")

    elif result.missing_requested:
        print("🟡 EPISTEMIC PAUSE")
        print("Missing information required:")
        for m in result.missing_requested:
            print(f" - {m}")

        plot_uncertainty(result.error_history, decision="REQUEST INFO")

    else:
        print("🔴 EPISTEMIC STOP")
        print(result.reason)
        plot_uncertainty(result.error_history, decision="STOP")


def main():
    run_flow(CHEST_PAIN_FLOW)


if __name__ == "__main__":
    main()
