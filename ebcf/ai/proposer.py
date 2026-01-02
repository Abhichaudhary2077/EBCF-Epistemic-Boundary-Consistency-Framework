class AIProposer:
    """
    Simulates an AI that always tries to give an answer.
    This is intentionally naive.
    """

    def propose(self, state):
        # Fake confidence — this is what AI tends to do
        return {
            "answer": "Likely cause identified based on patterns",
            "confidence": 0.85
        }
