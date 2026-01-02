from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class Assumption:
    id: str
    description: str
    status: str = "holding"  # holding | stressed | violated
    stress_score: float = 0.0


@dataclass
class EpistemicState:
    observables: Dict[str, Any]
    assumptions: Dict[str, Assumption]

    representations: Dict[str, Any] = field(default_factory=dict)
    residuals: Dict[str, Any] = field(default_factory=dict)
    uncertainty: Dict[str, float] = field(default_factory=dict)

    consistency_status: str = "improving"  # improving | stagnant | inconsistent
    history: List[Dict[str, Any]] = field(default_factory=list)

    error_history: List[float] = field(default_factory=list)