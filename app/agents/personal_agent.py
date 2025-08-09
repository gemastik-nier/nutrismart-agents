from google.adk.agents import LlmAgent
from config import MODEL_ID
from tools import user_profile_tool, user_calorie_history_tool

# Personal AI Agent: hits backend APIs for user data and calorie history
personal_agent = LlmAgent(
    model=MODEL_ID,
    name="PersonalAIAgent",
    description="Personal agent accessing user profile and calorie history via backend APIs",
    instruction="""
You help with personalization. Use the available API tools to retrieve user profile data and calorie history. Never invent user data; if missing, state what is needed.
""",
    tools=[user_profile_tool, user_calorie_history_tool],
)
