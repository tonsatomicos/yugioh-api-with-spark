from typing import Tuple

from core.interfaces.i_etl_service import IETLService
from core.interfaces.i_extract_service import IExtractService
from core.interfaces.i_load_service import ILoadService
from core.interfaces.i_transform_service import ITransformService
from core.utils.log_decorator import log_decorator
from core.utils.spark_session import get_spark_session
from pyspark.sql import DataFrame, SparkSession


class ETLService(IETLService):
    def __init__(
        self,
        extract_service: IExtractService,
        transform_service: ITransformService,
        load_service: ILoadService,
    ) -> None:
        self.data: DataFrame = None
        self.spark: SparkSession = None
        self.message: str = None
        self.success: bool = False
        self.extract_service = extract_service
        self.transform_service = transform_service
        self.load_service = load_service

    @log_decorator
    def extract_data(self) -> Tuple[str, bool]:
        return self.extract_service.extract_data()

    @log_decorator
    def transform_data(self, spark: SparkSession) -> Tuple[DataFrame, str, bool]:
        return self.transform_service.transform_data(spark)

    @log_decorator
    def load_data(self, data: DataFrame) -> Tuple[str, bool]:
        return self.load_service.load_data(data)

    @log_decorator
    def get_spark_session(self) -> Tuple[SparkSession, str, bool]:
        self.spark, self.message, self.success = get_spark_session()

    @log_decorator
    def orchestrator(self) -> None:
        self.get_spark_session()
        if self.success:
            self.message, self.success = self.extract_data()
            if self.success:
                self.data, self.message, self.success = self.transform_data(self.spark)
                if self.success:
                    self.message, self.success = self.load_data(self.data)
