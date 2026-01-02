def generate_human_report(boundary_record, state):
    print("========== EPISTEMIC REPORT ==========\n")

    print("Result:")
    print("Further uncertainty reduction is NOT possible with the current information.\n")

    print("Where understanding breaks:")
    print(f"- Structural location: {boundary_record.structural_location}\n")

    print("Which assumptions are responsible:")
    if boundary_record.assumption_context:
        for a in boundary_record.assumption_context:
            print(f"- {a}")
    else:
        print("- None explicitly violated")

    print("\nHow all models behaved:")
    print(f"- {boundary_record.representation_agreement}\n")

    print("Epistemic status (root cause):")
    print(f"- {boundary_record.epistemic_status}\n")

    print("Confidence in this conclusion:")
    print(f"- {boundary_record.confidence * 100:.1f}%\n")

    print("How much the system tried:")
    print(f"- Iterations attempted: {len(boundary_record.assumption_context)}")


    print("What this means:")
    print(
        "The system cannot progress further without new observables or "
        "a change in assumptions. Continuing would require guessing, "
        "which EBCF explicitly forbids."
    )

    print("\n=====================================")
