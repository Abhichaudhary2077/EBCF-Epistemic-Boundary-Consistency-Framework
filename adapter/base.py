from abc import ABC, abstractmethod


class SystemAdapter(ABC):

    @abstractmethod
    def fit_models(self, state):
        pass

    @abstractmethod
    def compute_error(self, state) -> float:
        pass

    @abstractmethod
    def update_assumptions(self, state):
        pass
