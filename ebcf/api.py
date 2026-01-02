from ebcf.core.state import EpistemicState, Assumption
from ebcf.core.consistency import ConsistencyMonitor
from ebcf.core.identifiability import IdentifiabilityAnalyzer
from ebcf.core.controller import EpistemicController


class EpistemicResult:
    def __init__(self, allowed, reason=None, confidence=None):
        self.allowed = allowed
        self.reason = reason
        self.confidence = confidence

    def __repr__(self):
        return (
            f"EpistemicResult(allowed={self.allowed}, "
            f"confidence={self.confidence}, reason={self.reason})"
        )


def epistemic_check(observables, missing=None, max_iter=5):
    """
    Minimal public API.

    Parameters:
    - observables: list of known information
    - missing: list of missing but relevant information
    - max_iter: epistemic effort limit

    Returns:
    - EpistemicResult
    """
    missing = missing or []

    assumptions = {
        item: Assumption(
            id=item,
            description=f"Required but missing information: {item}",
            status="violated"
        )
        for item in missing
    }

    state = EpistemicState(
        observables={"observables": observables},
        assumptions=assumptions
    )

    controller = EpistemicController(
        ConsistencyMonitor(),
        IdentifiabilityAnalyzer()
    )

    boundary = None
    for _ in range(max_iter):
        error = 1.0 if missing else 0.0
        boundary = controller.step(state, error)
        if boundary:
            break

    if boundary:
        return EpistemicResult(
            allowed=False,
            reason=boundary.epistemic_status,
            confidence=boundary.confidence
        )

    return EpistemicResult(
        allowed=True,
        reason="No epistemic boundary detected",
        confidence=1.0
    )
