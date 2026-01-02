from ebcf.core.state import EpistemicState, Assumption
from ebcf.core.consistency import ConsistencyMonitor
from ebcf.core.identifiability import IdentifiabilityAnalyzer
from ebcf.core.controller import EpistemicController
from ebcf.reporting.reporting_text import generate_human_report


def parse_list(text):
    if not text.strip():
        return []
    return [x.strip() for x in text.split(",")]


def main():
    print("\n=== EBCF — Epistemic Boundary Checker ===\n")

    domain = input("What is the domain? (e.g. medical, ML, research): ").strip()

    observables_input = input(
        "List observables you currently have (comma separated): "
    )
    observables_list = parse_list(observables_input)

    missing_input = input(
        "List important things you do NOT have (comma separated): "
    )
    missing_list = parse_list(missing_input)

    # Build observables dict
    observables = {
        "domain": domain,
        "observables": observables_list,
        "missing": missing_list
    }

    # Each missing item becomes an assumption
    assumptions = {}
    for item in missing_list:
        assumptions[item] = Assumption(
            id=item,
            description=f"Missing but assumed unnecessary: {item}"
        )

    state = EpistemicState(
        observables=observables,
        assumptions=assumptions
    )

    controller = EpistemicController(
        ConsistencyMonitor(),
        IdentifiabilityAnalyzer()
    )

    # Minimal epistemic loop
    boundary = None
    for _ in range(5):
        # Artificial error: if things are missing, error does not improve
        error = 1.0 if missing_list else 0.0
        boundary = controller.step(state, error)
        if boundary:
            break

    print("\n--- EBCF DECISION ---")

    if boundary:
        generate_human_report(boundary, state)
    else:
        print(
            "No epistemic boundary detected.\n"
            "Answering MAY be allowed with current information."
        )


if __name__ == "__main__":
    main()
