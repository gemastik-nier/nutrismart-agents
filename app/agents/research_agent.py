from google.adk.agents import LlmAgent
from config import MODEL_ID
from tools import web_search, latest_nutrition_facts_tool

# Research AI Agent: can use web search and latest nutrition facts API
research_agent = LlmAgent(
    model=MODEL_ID,
    name="ResearchAIAgent",
    description="Researches nutrition topics using web search and latest nutrition facts API",
    instruction="""
You are a research specialist. Use web search for broad context and the latest nutrition facts API for concrete data points. Always cite sources and prefer authoritative references.
""",
    tools=[web_search, latest_nutrition_facts_tool],
)
