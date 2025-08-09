from google.adk.agents import LlmAgent
from config import MODEL_ID
from tools import local_rag_tool

# Nutritionist AI Agent: backed by local RAG knowledge source
nutritionist_rag_agent = LlmAgent(
    model=MODEL_ID,
    name="NutritionistRAGAgent",
    description="Nutritionist agent using RAG over prepared knowledge sources",
    instruction="""
You are a licensed-style nutritionist assistant. Ground your answers using the provided RAG tool that accesses curated knowledge sources we maintain. Quote or summarize relevant snippets and keep advice educational.
""",
    tools=[local_rag_tool],
)
