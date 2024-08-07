from abc import ABC, abstractmethod
from typing import Tuple


class ILoadService(ABC):
    @abstractmethod
    def load_data(self) -> Tuple[str, bool]:
        pass
