from ebcf.flows.chest_pain import CHEST_PAIN_FLOW
from ebcf import epistemic_check


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
            if q["type"] == "choice":
                answer = ask_choice(q)
            elif q["type"] == "multi_choice":
                answer = ask_multi_choice(q)
            else:
                raise ValueError(f"Unknown question type: {q['type']}")

            observables[q["id"]] = answer

            # Hard-stop logic (red flags)
            if q.get("hard_stop") and "none" not in answer:
                hard_stop = True
                break

        if hard_stop:
            break

    print("\n--- EBCF VERDICT ---\n")

    if hard_stop:
        print("Epistemic STOP:")
        print("Red-flag indicators detected.")
        print("Do not reason further. Seek urgent medical care.")
        return

    # Pass structured observables into EBCF
    result = epistemic_check(
        observables=observables,
        missing=["clinical_tests"]
    )

    if result.allowed:
        print("Reasoning allowed.")
        print("Current information is sufficient to proceed without guessing.")
    else:
        print("Epistemic STOP:")
        print(result.reason)

def main():
    run_flow(CHEST_PAIN_FLOW)


if __name__ == "__main__":
    main()