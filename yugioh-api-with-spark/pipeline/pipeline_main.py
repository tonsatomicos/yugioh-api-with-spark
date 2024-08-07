import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.config.logging_config import configure_logging
from core.services.etl.etl_service import ETLService
from core.services.extract.extract_service import ExtractService
from core.services.load.load_service import LoadService
from core.services.transform.transform_service import TransformService

configure_logging()


def main():
    # extract
    start_date = "2000-01-01"
    end_date = "2024-08-03"
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?&startdate={start_date}&enddate={end_date}"
    # transform
    base_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../data/input")
    )
    # load
    output_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../data/output/yugioh-tcg")
    )
    #
    extract_service = ExtractService(url, base_path)
    transform_service = TransformService(base_path)
    load_service = LoadService(output_path)
    #
    etl_batch = ETLService(extract_service, transform_service, load_service)
    etl_batch.orchestrator()


if __name__ == "__main__":
    main()
