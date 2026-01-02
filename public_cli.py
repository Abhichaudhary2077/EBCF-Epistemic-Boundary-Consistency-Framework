from ebcf import epistemic_check


def ask_list(prompt):
    text = input(prompt).strip()
    if not text:
        return []
    return [x.strip() for x in text.split(",")]


def main():
    print("\n=== EBCF — Honest Reasoning Checker ===\n")
    print("This tool checks whether answering a question would require guessing.\n")

    print("Choose a mode:")
    print("1) General situation")
    print("2) Health / medical")
    print("3) Research / science")
    print("4) Custom / advanced")

    choice = input("\nEnter choice (1–4): ").strip()

    print("\nTell me what you KNOW.")
    observables = ask_list("List things you are sure about (comma separated): ")

    print("\nTell me what you do NOT know.")
    missing = ask_list("List important missing information (comma separated): ")

    result = epistemic_check(
        observables=observables,
        missing=missing
    )

    print("\n--- EBCF VERDICT ---\n")

    if result.allowed:
        print("✅ It is epistemically allowed to proceed.")
        print(f"Confidence: {result.confidence:.2f}")
    else:
        print("❌ Stop. Answering would require guessing.")
        print(f"Reason: {result.reason}")
        print(f"Confidence: {result.confidence:.2f}")

    print("\nRemember:")
    print("Not knowing yet is not failure. Guessing is.")


if __name__ == "__main__":
    main()
