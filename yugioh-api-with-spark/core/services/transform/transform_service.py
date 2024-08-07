from typing import Tuple

from core.interfaces.i_transform_service import ITransformService
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import (
    ArrayType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)


class TransformService(ITransformService):
    def __init__(self, path: str) -> None:
        self.path: str = path

    def transform_data(self, spark: SparkSession) -> Tuple[DataFrame, str, bool]:
        try:
            schema = StructType(
                [
                    StructField("archetype", StringType(), True),
                    StructField("atk", IntegerType(), True),
                    StructField("attribute", StringType(), True),
                    StructField(
                        "banlist_info",
                        StructType(
                            [
                                StructField("ban_goat", StringType(), True),
                                StructField("ban_ocg", StringType(), True),
                                StructField("ban_tcg", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "card_images",
                        ArrayType(
                            StructType(
                                [
                                    StructField("id", IntegerType(), True),
                                    StructField("image_url", StringType(), True),
                                    StructField(
                                        "image_url_cropped", StringType(), True
                                    ),
                                    StructField("image_url_small", StringType(), True),
                                ]
                            )
                        ),
                        True,
                    ),
                    StructField(
                        "card_prices",
                        ArrayType(
                            StructType(
                                [
                                    StructField("amazon_price", StringType(), True),
                                    StructField("cardmarket_price", StringType(), True),
                                    StructField(
                                        "coolstuffinc_price", StringType(), True
                                    ),
                                    StructField("ebay_price", StringType(), True),
                                    StructField("tcgplayer_price", StringType(), True),
                                ]
                            )
                        ),
                        True,
                    ),
                    StructField(
                        "card_sets",
                        ArrayType(
                            StructType(
                                [
                                    StructField("set_code", StringType(), True),
                                    StructField("set_name", StringType(), True),
                                    StructField("set_price", StringType(), True),
                                    StructField("set_rarity", StringType(), True),
                                    StructField("set_rarity_code", StringType(), True),
                                ]
                            )
                        ),
                        True,
                    ),
                    StructField("date_ingestion", TimestampType(), True),
                    StructField("def", IntegerType(), True),
                    StructField("desc", StringType(), True),
                    StructField("frameType", StringType(), True),
                    StructField("id", IntegerType(), True),
                    StructField("level", IntegerType(), True),
                    StructField("linkmarkers", ArrayType(StringType()), True),
                    StructField("linkval", IntegerType(), True),
                    StructField("monster_desc", StringType(), True),
                    StructField("name", StringType(), True),
                    StructField("pend_desc", StringType(), True),
                    StructField("race", StringType(), True),
                    StructField("scale", IntegerType(), True),
                    StructField("type", StringType(), True),
                    StructField("ygoprodeck_url", StringType(), True),
                ]
            )

            df = spark.read.schema(schema).option("multiline", "true").json(self.path)

            df.createOrReplaceTempView("yugioh")

            result_df = spark.sql(
                """
            SELECT
                A.id id_card,
                A.name name_card,
                A.type type_card,
                A.frameType frame_type_card,
                A.race race_card,
                IFNULL(A.archetype, 'N/I') archetype_card,
                IFNULL(A.scale, 'N/I') scale_card,
                A.desc description_card,
                IFNULL(A.atk, 0) atk_card,
                IFNULL(A.def, 0) def_card,
                IFNULL(A.level, 0) level_card,
                card_set.set_name card_set_name_card,
                card_set.set_code card_set_code_card,
                card_set.set_rarity card_set_rarity_card,
                card_set.set_rarity_code card_set_rarity_code_card,
                card_set.set_price card_set_price_card,
                card_price.amazon_price amazon_price_card,
                card_price.cardmarket_price cardmarket_price_card,
                card_price.coolstuffinc_price coolstuffinc_price_card,
                card_price.ebay_price ebay_price_card,
                card_price.tcgplayer_price tcgplayer_price_card,
                card_image.image_url image_url_card,
                card_image.image_url_cropped image_url_cropped_card,
                card_image.image_url_small image_url_small_card,
                IFNULL(A.banlist_info.ban_goat, 'N/I') ban_goat_card,
                IFNULL(A.banlist_info.ban_ocg, 'N/I') ban_ocg_card,
                IFNULL(A.banlist_info.ban_tcg, 'N/I') ban_tcg_card,
                A.date_ingestion,
                A.ygoprodeck_url
            FROM yugioh A
            LATERAL VIEW explode(card_sets) card_set AS card_set
            LATERAL VIEW explode(card_prices) card_price AS card_price
            LATERAL VIEW explode(card_images) card_image as card_image
            WHERE 1=1
            """
            )

            return result_df, "Success in transforming data.", True

        except Exception as e:
            return DataFrame, f"Error: {e}", False
