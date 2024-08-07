from typing import Tuple

from pyspark.sql import SparkSession


def get_spark_session() -> Tuple[SparkSession, str, bool]:
    try:
        spark = (
            SparkSession.builder.appName("yugioh-api")
            .master("spark://spark-master:7077")
            .getOrCreate()
        )

        sc = spark.sparkContext
        if sc is not None and not sc._jsc.sc().isStopped():
            return spark, "", True
        else:
            return spark, "SparkContext isn't active.", False

    except Exception as e:
        return spark, f"Error: {e}", False
