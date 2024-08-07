from typing import Tuple

from core.interfaces.i_load_service import ILoadService
from pyspark.sql import DataFrame


class LoadService(ILoadService):
    def __init__(self, path: str) -> None:
        self.path: str = path

    def load_data(self, data: DataFrame) -> Tuple[str, bool]:
        try:
            path = self.path
            data.write.partitionBy("type_card").mode("overwrite").parquet(path)

            return "Successful loading data.", True

        except Exception as e:
            return f"Error: {e}", False
