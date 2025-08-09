from typing import Dict, Optional
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json

from google.adk.tools import FunctionTool
from config import BE_URL


def get_latest_nutrition_facts(food_name: str, serving_size: Optional[str] = None) -> Dict:
    """Fetch latest nutrition facts for a food from backend API.

    Args:
        food_name: Food item name to look up.
        serving_size: Optional serving descriptor, e.g., "100g", "1 cup".

    Returns:
        JSON dictionary from backend or an error structure.
    """
    try:
        query = {"food_name": food_name}
        if serving_size:
            query["serving_size"] = serving_size
        query_string = urlencode(query)
        url = f"{BE_URL.rstrip('/')}/nutrition/facts?{query_string}"
        req = Request(url, headers={"Accept": "application/json"})
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"status": "success", "source": url, "data": data}
    except Exception as exc:  # Fallback to informative error
        return {
            "status": "error",
            "error_message": f"Failed to fetch latest nutrition facts: {exc}",
            "hint": "Ensure BE_URL is correctly set and backend is reachable",
            "food_name": food_name,
            "serving_size": serving_size,
        }


latest_nutrition_facts_tool = FunctionTool(func=get_latest_nutrition_facts)
