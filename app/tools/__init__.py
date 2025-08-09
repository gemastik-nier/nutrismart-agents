from google.adk.tools import google_search
from .nutrition_latest import latest_nutrition_facts_tool
from .personal_api import user_profile_tool, user_calorie_history_tool
from .local_rag import local_rag_tool

# Create a web search tool for agents to use
web_search = google_search

__all__ = [
    "web_search",
    "latest_nutrition_facts_tool",
    "user_profile_tool",
    "user_calorie_history_tool",
    "local_rag_tool",
]