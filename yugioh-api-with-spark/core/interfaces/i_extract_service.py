from abc import ABC, abstractmethod
from typing import Tuple


class IExtractService(ABC):
    @abstractmethod
    def extract_data(self) -> Tuple[str, bool]:
        pass
