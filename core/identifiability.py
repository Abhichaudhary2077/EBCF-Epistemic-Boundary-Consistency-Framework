class IdentifiabilityAnalyzer:
    def check(self, state) -> bool:
        """
        Returns True if identifiable in principle,
        False if non-identifiable.
        Conservative by default.
        """
        return False
