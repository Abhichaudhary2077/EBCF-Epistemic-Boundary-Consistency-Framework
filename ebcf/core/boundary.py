from dataclasses import dataclass
from typing import List


@dataclass
class BoundaryRecord:
    structural_location: str
    assumption_context: List[str]
    representation_agreement: str
    epistemic_status: str
    confidence: float
