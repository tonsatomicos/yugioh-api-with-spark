from typing import Any, Dict

import requests


def http_get(url: str) -> Dict[str, Any]:
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()
