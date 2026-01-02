from ebcf_cli import parse_list
from core.state import EpistemicState, Assumption
from core.consistency import ConsistencyMonitor
from core.identifiability import IdentifiabilityAnalyzer
from core.controller import EpistemicController


def main():
    print("\n=== Can This Question Be Answered? ===\n")

    problem = input("Briefly describe your problem:\n> ").strip()

    known = input(
        "\nWhat information do you already have? (comma separated)\n> "
    )
    known_list = parse_list(known)

    missing = input(
        "\nIs there important information you do NOT have yet? (yes/no)\n> "
    ).strip().lower()

    missing_items = []
    if missing == "yes":
        missing_items = parse_list(
            input("List missing information (comma separated):\n> ")
        )

    # Build epistemic state (hidden from user)
    observables = {
        "problem": problem,
        "known_info": known_list
    }

    assumptions = {}
    for item in missing_items:
        assumptions[item] = Assumption(
            id=item,
            description=f"Required but missing information: {item}",
            status="violated"
        )

    state = EpistemicState(
        observables=observables,
        assumptions=assumptions
    )

    controller = EpistemicController(
        ConsistencyMonitor(),
        IdentifiabilityAnalyzer()
    )

    boundary = None
    for _ in range(5):
        error = 1.0 if missing_items else 0.0
        boundary = controller.step(state, error)
        if boundary:
            break

    print("\n--- VERDICT ---\n")

    if boundary:
        print("❌ A reliable answer is NOT possible right now.\n")
        print("Why?")
        print(
            "There is not enough information to rule out multiple possibilities."
        )
        print("\nWhat would help?")
        if missing_items:
            for item in missing_items:
                print(f"- {item}")
        else:
            print("- Additional relevant information")
    else:
        print("✅ A reliable answer MAY be possible with current information.")
        print("Proceed carefully.")

    print("\n(This tool does not give answers — it checks if answers are trustworthy.)")


if __name__ == "__main__":
    main()
