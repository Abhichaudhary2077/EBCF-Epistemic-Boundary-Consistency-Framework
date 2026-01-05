from ebcf.core.state import EpistemicState, Assumption
from ebcf.core.consistency import ConsistencyMonitor
from ebcf.core.identifiability import IdentifiabilityAnalyzer
from ebcf.core.controller import EpistemicController


class EpistemicResult:
    def __init__(
        self,
        allowed,
        reason=None,
        confidence=None,
        error_history=None,
        missing_requested=None
    ):
        self.allowed = allowed
        self.reason = reason
        self.confidence = confidence
        self.error_history = error_history or []
        self.missing_requested = missing_requested or []

    def __repr__(self):
        return (
            f"EpistemicResult("
            f"allowed={self.allowed}, "
            f"confidence={self.confidence}, "
            f"reason={self.reason}, "
            f"missing_requested={self.missing_requested}"
            f")"
        )


def epistemic_check(observables, missing=None, max_iter=5):
    missing = missing or []

    assumptions = {
        item: Assumption(
            id=item,
            description=f"Required but missing information: {item}",
            status="stressed"   # 🔴 NOT violated
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

    # 🔴 Irreducible epistemic failure
    if boundary and not missing:
        return EpistemicResult(
            allowed=False,
            reason=boundary.epistemic_status,
            confidence=boundary.confidence,
            error_history=state.error_history
        )

    # 🟡 Reducible uncertainty → request info
    if missing:
        return EpistemicResult(
            allowed=False,
            reason="Additional information required before reasoning",
            confidence=0.5,
            error_history=state.error_history,
            missing_requested=missing
        )

    # 🟢 Allowed
    return EpistemicResult(
        allowed=True,
        reason="Reasoning epistemically justified",
        confidence=1.0,
        error_history=state.error_history
    )
