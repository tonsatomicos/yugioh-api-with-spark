import json
import os
from datetime import datetime
from typing import Any, Dict, Tuple

import requests
from core.interfaces.i_extract_service import IExtractService
from core.utils.http_utils import http_get


class ExtractService(IExtractService):
    def __init__(self, end_point: str, path: str) -> None:
        self.end_point: str = end_point
        self.path: str = path

    def extract_data(self) -> Tuple[str, bool]:
        try:
            data = http_get(self.end_point)

            if data:
                date_ingestion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                now = datetime.now().strftime("%Y%m%d_%H%M%S.%f")
                self.save_data(data, self.path, date_ingestion, now)
                return "Success in extracting data.", True
            else:
                return "No data returned by the endpoint.", False

        except requests.RequestException as e:
            return f"Error in HTTP request: {e}", False

        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}", False

        except Exception as e:
            return f"Error: {e}", False

    def save_data(
        self, data: Dict[str, Any], path: str, date_ingestion: str, now: str
    ) -> None:
        cards_data = data.get("data", [])
        for card in cards_data:
            card["date_ingestion"] = date_ingestion

        filename = os.path.join(path, f"{now}.json")
        with open(filename, "w") as open_file:
            json.dump(cards_data, open_file, indent=4)
