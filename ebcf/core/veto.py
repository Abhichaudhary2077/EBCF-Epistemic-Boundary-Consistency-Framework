def epistemic_veto(boundary_record, proposal):
    """
    Rejects AI proposals when epistemic boundaries exist.
    """
    if boundary_record is not None:
        return {
            "status": "REJECTED",
            "reason": "Epistemic boundary detected — answering would require guessing"
        }

    return {
        "status": "APPROVED",
        "answer": proposal
    }
