from typing import Dict, Optional
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json

from google.adk.tools import FunctionTool
from config import BE_URL


def get_user_profile(user_id: str) -> Dict:
    """Fetch user profile data from backend.

    Expected backend endpoint: GET {BE_URL}/users/{user_id}
    """
    try:
        url = f"{BE_URL.rstrip('/')}/users/{user_id}"
        req = Request(url, headers={"Accept": "application/json"})
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"status": "success", "source": url, "data": data}
    except Exception as exc:
        return {"status": "error", "error_message": str(exc), "user_id": user_id}


def get_user_calorie_history(user_id: str, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict:
    """Fetch user calorie tracking history.

    Expected endpoint: GET {BE_URL}/users/{user_id}/calories?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
    """
    try:
        query = {}
        if start_date:
            query["start_date"] = start_date
        if end_date:
            query["end_date"] = end_date
        qs = urlencode(query)
        url = f"{BE_URL.rstrip('/')}/users/{user_id}/calories"
        if qs:
            url = f"{url}?{qs}"
        req = Request(url, headers={"Accept": "application/json"})
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"status": "success", "source": url, "data": data}
    except Exception as exc:
        return {"status": "error", "error_message": str(exc), "user_id": user_id, "start_date": start_date, "end_date": end_date}


user_profile_tool = FunctionTool(func=get_user_profile)
user_calorie_history_tool = FunctionTool(func=get_user_calorie_history)
