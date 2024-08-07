from abc import ABC, abstractmethod
from typing import Tuple

from pyspark.sql import DataFrame


class ITransformService(ABC):
    @abstractmethod
    def transform_data(self) -> Tuple[DataFrame, str, bool]:
        pass
