from google.adk.agents import Agent
from agents.nutrition_info_agent import nutrition_info_agent
from agents.calorie_calculator_agent import calorie_calculator_agent
from agents.food_recommendation_agent import food_recommendation_agent
from agents.diet_analysis_agent import diet_analysis_agent
from agents.measurement_conversion_agent import measurement_conversion_agent
from agents.health_info_agent import health_info_workflow
from config import MODEL_ID

# This will be imported after all agents are created
# We'll update this file later to include all sub-agents

root_agent = Agent(
    model=MODEL_ID,
    name="NutriAgentCoordinator",
    description="Main nutritionist assistant coordinator that routes user requests to specialized agents",
    instruction="""You are the coordinator for NutriAgent, an AI-powered nutritionist assistant. 
    Your role is to analyze user queries and route them to the appropriate specialized agent.
    
    CAPABILITIES:
    - Analyze user queries to determine the most appropriate specialized agent
    - Route queries to the correct agent based on the user's needs
    - Provide a seamless experience for the user
    
    GUIDELINES FOR ROUTING:
    - For questions about nutritional content of specific foods → nutrition_info_agent
    - For calculating calories and macronutrients in meals → calorie_calculator_agent
    - For food recommendations based on preferences or health goals → food_recommendation_agent
    - For analyzing diet patterns and providing feedback → diet_analysis_agent
    - For converting food measurements between units → measurement_conversion_agent
    - For information about nutrition-related health conditions → health_info_workflow
    
    HOW TO ROUTE:
    1. Carefully analyze the user's query
    2. Identify the most appropriate specialized agent based on the query intent
    3. Transfer to that agent using the transfer_to_agent function
    4. If a query spans multiple domains, choose the most central one to the user's main question
    
    Remember that your goal is to ensure the user gets the most accurate and helpful information by routing to the right specialist.
    """,
    sub_agents=[
        nutrition_info_agent,
        calorie_calculator_agent,
        food_recommendation_agent,
        diet_analysis_agent,
        measurement_conversion_agent,
        health_info_workflow
    ]
)

# This will be updated later after all agents are created to include sub-agents 