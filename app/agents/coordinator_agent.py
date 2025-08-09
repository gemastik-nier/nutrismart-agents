from google.adk.agents import Agent
from config import MODEL_ID
from agents.research_agent import research_agent
from agents.nutritionist_rag_agent import nutritionist_rag_agent
from agents.personal_agent import personal_agent

# Coordinator that delegates to 3 specialized agents per new schema
root_agent = Agent(
    model=MODEL_ID,
    name="NutriAgentCoordinator",
    description="Coordinator that delegates to Research, Nutritionist (RAG), and Personal agents",
    instruction="""
You coordinate three specialists:
1) Research AI Agent — for web research and latest nutrition facts
2) Nutritionist AI Agent (RAG) — for grounded guidance using our curated knowledge sources
3) Personal AI Agent — for user-specific data via backend APIs

ROUTING RULES:
- If the task needs web search or latest nutrition facts → ResearchAIAgent
- If the task needs domain guidance, explanations, or knowledge-base grounding → NutritionistRAGAgent
- If the task needs user data (profile, history, personalization) → PersonalAIAgent

Prefer a single handoff. If a query spans domains, choose the primary intent; mention any limitations.
""",
    sub_agents=[
        research_agent,
        nutritionist_rag_agent,
        personal_agent,
    ],
)
