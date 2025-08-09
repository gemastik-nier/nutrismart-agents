# NutriAgent Tools

This directory contains the tools for the NutriAgent, a nutritionist AI agent that provides information and recommendations about nutrition, diet, and health.

## Overview

The tools in this directory are built using Google's Agent Development Kit (ADK) and follow the principles outlined in the [ADK Tools documentation](https://google.github.io/adk-docs/tools/). Each tool is implemented as a `FunctionTool` that can be used by the agent to perform specific tasks related to nutrition and diet.

## Tools

### 1. Nutrition Information Tool (`nutrition_info.py`)

Retrieves nutritional information for specific foods.

**Usage:**
- When a user asks about the nutritional content of a specific food
- When the agent needs to look up vitamins, minerals, or other nutrients in a food

**Example Input:**
```python
{
    "food_name": "apple",
    "quantity": 1,
    "unit": "piece"
}
```

**Example Output:**
```python
{
    "status": "success",
    "food_name": "apple",
    "quantity": 1,
    "unit": "piece",
    "calories": 62.4,
    "macronutrients": {
        "protein": 0.4,
        "carbohydrates": 16.6,
        "fat": 0.2,
        "fiber": 2.9
    },
    "micronutrients": {
        "vitamin_c": "4.6 mg",
        "potassium": "107 mg"
    }
}
```

### 2. Calorie Calculator Tool (`calorie_calculator.py`)

Calculates total calories and macronutrients for a list of food items.

**Usage:**
- When a user wants to know the nutritional content of a meal or recipe
- When calculating the total nutritional value of multiple foods

**Example Input:**
```python
{
    "food_items": [
        {
            "name": "chicken breast",
            "quantity": 100,
            "unit": "g"
        },
        {
            "name": "broccoli",
            "quantity": 1,
            "unit": "cup"
        },
        {
            "name": "rice",
            "quantity": 0.5,
            "unit": "cup"
        }
    ]
}
```

**Example Output:**
```python
{
    "status": "success",
    "total_calories": 256.3,
    "total_macronutrients": {
        "protein": 37.5,
        "carbohydrates": 22.9,
        "fat": 4.2,
        "fiber": 2.7
    },
    "items_calculated": ["chicken breast", "broccoli", "rice"],
    "items_not_found": []
}
```

### 3. Food Recommendation Tool (`food_recommendation.py`)

Recommends foods based on dietary preferences, health goals, and restrictions.

**Usage:**
- When a user asks for food recommendations based on their diet or health goals
- When suggesting alternatives for foods that need to be avoided

**Example Input:**
```python
{
    "dietary_preferences": ["vegetarian"],
    "health_goals": ["heart health"],
    "allergies": ["nuts"],
    "nutrient_focus": "protein"
}
```

**Example Output:**
```python
{
    "status": "success",
    "recommendations": [
        {
            "food": "tofu",
            "category": "protein",
            "benefits": ["heart health", "bone health"],
            "nutrients": ["protein", "calcium", "iron"],
            "serving_suggestion": "85g (3oz) firm tofu, stir-fried or baked"
        },
        {
            "food": "lentils",
            "category": "protein",
            "benefits": ["heart health", "digestive health", "blood sugar control"],
            "nutrients": ["protein", "fiber", "iron", "folate"],
            "serving_suggestion": "1/2 cup cooked in soups or as a side dish"
        }
    ]
}
```

### 4. Diet Analysis Tool (`diet_analysis.py`)

Analyzes a user's diet based on their food log and provides nutritional insights.

**Usage:**
- When a user wants to analyze their current diet
- When identifying nutritional gaps or excesses in a diet

**Example Input:**
```python
{
    "food_log": [
        {
            "food": "apple",
            "quantity": 1,
            "unit": "piece",
            "meal_type": "breakfast"
        },
        {
            "food": "chicken breast",
            "quantity": 100,
            "unit": "g",
            "meal_type": "lunch"
        },
        {
            "food": "broccoli",
            "quantity": 1,
            "unit": "cup",
            "meal_type": "dinner"
        }
    ]
}
```

**Example Output:**
```python
{
    "status": "success",
    "total_calories": 251.4,
    "macronutrient_distribution": {
        "protein_percent": 52.3,
        "carbohydrates_percent": 32.6,
        "fat_percent": 15.1
    },
    "nutritional_analysis": {
        "strengths": ["Adequate protein intake", "Good vegetable consumption"],
        "gaps": ["Low fiber intake", "Low fruit intake"],
        "recommendations": ["Increase consumption of fruits, vegetables, and whole grains"]
    },
    "meal_pattern_analysis": "You have a good meal frequency."
}
```

### 5. Measurement Conversion Tool (`measurement_conversion.py`)

Converts food measurements from one unit to another.

**Usage:**
- When a user needs to convert between different units of measurement
- When following recipes that use unfamiliar measurement units

**Example Input:**
```python
{
    "food": "flour",
    "amount": 1,
    "from_unit": "cup",
    "to_unit": "g"
}
```

**Example Output:**
```python
{
    "status": "success",
    "food": "flour",
    "original_amount": 1,
    "original_unit": "cup",
    "converted_amount": 125.4,
    "converted_unit": "g"
}
```

### 6. Health Condition Information Tool (`health_condition_info.py`)

Provides information about nutrition-related health conditions.

**Usage:**
- When a user asks about dietary considerations for specific health conditions
- When providing general information about nutrition-related health conditions

**Example Input:**
```python
{
    "condition": "diabetes"
}
```

**Example Output:**
```python
{
    "status": "success",
    "condition_name": "Diabetes",
    "description": "Diabetes is a chronic condition characterized by high levels of glucose in the blood...",
    "nutritional_considerations": [
        "Monitor carbohydrate intake to help manage blood sugar levels",
        "Maintain consistent meal timing to help regulate blood glucose",
        "Focus on foods with a low glycemic index",
        "Balance meals with protein, healthy fats, and fiber",
        "Stay well-hydrated with water rather than sugary beverages"
    ],
    "foods_to_include": [
        "Non-starchy vegetables (leafy greens, broccoli, peppers)",
        "Whole grains (brown rice, quinoa, whole wheat bread in moderation)",
        "Lean proteins (chicken, fish, tofu, legumes)",
        "Healthy fats (avocados, nuts, olive oil)",
        "Low-glycemic fruits (berries, apples, pears)"
    ],
    "foods_to_limit": [
        "Refined carbohydrates (white bread, white rice, pastries)",
        "Sugary foods and beverages",
        "Processed foods high in added sugars",
        "Fruit juices (even 100% juice) due to concentrated sugars",
        "Alcohol (can cause blood sugar fluctuations)"
    ],
    "disclaimer": "IMPORTANT: This information is for educational purposes only and is not intended as medical advice..."
}
```

## Using These Tools

To use these tools with the NutriAgent, import them in your agent definition:

```python
from google.adk.agents import Agent
from tools import (
    nutrition_info_tool,
    calorie_calculator_tool,
    food_recommendation_tool,
    diet_analysis_tool,
    measurement_conversion_tool,
    health_condition_info_tool,
    latest_nutrition_facts_tool,
    user_profile_tool,
    user_calorie_history_tool,
    local_rag_tool,
)

# Example: building a custom agent with new tools
nutritionist_agent = Agent(
    model="gemini-2.0-flash",
    name="NutriAgent",
    instruction="Use available tools to answer nutrition questions.",
    tools=[
        nutrition_info_tool,
        calorie_calculator_tool,
        food_recommendation_tool,
        diet_analysis_tool,
        measurement_conversion_tool,
        health_condition_info_tool,
        latest_nutrition_facts_tool,
        user_profile_tool,
        user_calorie_history_tool,
        local_rag_tool,
    ]
)
```

## Important Notes

- The tools currently use mock data for demonstration purposes. In a production environment, they should be connected to comprehensive nutrition databases or APIs.
- The health condition information tool provides general educational information only and is not a substitute for professional medical advice.
- These tools can be extended or modified to suit specific requirements or to include additional functionality. 