from abc import ABC, abstractmethod
from typing import Tuple

from pyspark.sql import DataFrame


class IETLService(ABC):
    @abstractmethod
    def extract_data(self) -> Tuple[str, bool]:
        pass

    @abstractmethod
    def transform_data(self) -> Tuple[DataFrame, str, bool]:
        pass

    @abstractmethod
    def load_data(self, data: DataFrame) -> Tuple[str, bool]:
        pass

    @abstractmethod
    def orchestrator(self) -> None:
        pass
