from google.adk.tools import FunctionTool
from typing import Dict, List, Optional

def recommend_foods(
    dietary_preferences: List[str] = None,
    health_goals: List[str] = None,
    allergies: List[str] = None,
    nutrient_focus: str = None
) -> Dict:
    """Recommends foods based on user preferences, health goals, and dietary restrictions.
    
    Use this tool when the user is looking for food recommendations based on their
    dietary preferences, health goals, allergies, or specific nutrient needs.
    
    Args:
        dietary_preferences: List of dietary preferences (e.g., ["vegetarian", "vegan", "keto", "paleo"])
        health_goals: List of health goals (e.g., ["weight loss", "muscle gain", "heart health", "diabetes management"])
        allergies: List of allergies or foods to avoid (e.g., ["nuts", "dairy", "gluten", "shellfish"])
        nutrient_focus: Specific nutrient the user wants to focus on (e.g., "protein", "fiber", "iron", "calcium")
    
    Returns:
        A dictionary with the following structure:
        {
            "status": "success" or "error",
            "recommendations": [
                {
                    "food": name of the recommended food,
                    "category": food category (e.g., "protein", "vegetable", "fruit"),
                    "benefits": list of health benefits,
                    "nutrients": list of key nutrients,
                    "serving_suggestion": recommended serving size and preparation
                },
                ...
            ],
            "error_message": description of error (only if status is "error")
        }
    """
    # In a real implementation, this would use a recommendation algorithm
    # based on a comprehensive food database
    # For demonstration, we'll use a simplified rule-based approach
    
    # Initialize empty lists if None is provided
    if dietary_preferences is None:
        dietary_preferences = []
    if health_goals is None:
        health_goals = []
    if allergies is None:
        allergies = []
    
    # Convert all inputs to lowercase for case-insensitive matching
    dietary_preferences = [pref.lower() for pref in dietary_preferences]
    health_goals = [goal.lower() for goal in health_goals]
    allergies = [allergy.lower() for allergy in allergies]
    if nutrient_focus:
        nutrient_focus = nutrient_focus.lower()
    
    # Food database with categories and properties
    food_database = {
        "chicken breast": {
            "category": "protein",
            "dietary_tags": ["high_protein", "low_carb"],
            "allergies": [],
            "nutrients": ["protein", "vitamin B6", "niacin"],
            "benefits": ["muscle building", "weight management"],
            "serving_suggestion": "85g (3oz) grilled or baked"
        },
        "salmon": {
            "category": "protein",
            "dietary_tags": ["high_protein", "keto", "paleo"],
            "allergies": ["fish", "seafood"],
            "nutrients": ["protein", "omega-3 fatty acids", "vitamin D"],
            "benefits": ["heart health", "brain health", "anti-inflammatory"],
            "serving_suggestion": "85g (3oz) baked or grilled with herbs"
        },
        "tofu": {
            "category": "protein",
            "dietary_tags": ["vegetarian", "vegan", "plant_based"],
            "allergies": ["soy"],
            "nutrients": ["protein", "calcium", "iron"],
            "benefits": ["heart health", "bone health"],
            "serving_suggestion": "85g (3oz) firm tofu, stir-fried or baked"
        },
        "lentils": {
            "category": "protein",
            "dietary_tags": ["vegetarian", "vegan", "plant_based", "high_fiber"],
            "allergies": [],
            "nutrients": ["protein", "fiber", "iron", "folate"],
            "benefits": ["heart health", "digestive health", "blood sugar control"],
            "serving_suggestion": "1/2 cup cooked in soups or as a side dish"
        },
        "spinach": {
            "category": "vegetable",
            "dietary_tags": ["vegetarian", "vegan", "plant_based", "keto", "paleo"],
            "allergies": [],
            "nutrients": ["iron", "calcium", "vitamin K", "vitamin A"],
            "benefits": ["bone health", "immune support", "eye health"],
            "serving_suggestion": "1 cup raw in salads or smoothies, or 1/2 cup cooked"
        },
        "broccoli": {
            "category": "vegetable",
            "dietary_tags": ["vegetarian", "vegan", "plant_based", "keto", "paleo"],
            "allergies": [],
            "nutrients": ["vitamin C", "fiber", "calcium", "folate"],
            "benefits": ["immune support", "digestive health", "cancer prevention"],
            "serving_suggestion": "1 cup chopped, steamed or roasted"
        },
        "avocado": {
            "category": "fruit",
            "dietary_tags": ["vegetarian", "vegan", "plant_based", "keto", "paleo"],
            "allergies": [],
            "nutrients": ["healthy fats", "fiber", "potassium", "vitamin E"],
            "benefits": ["heart health", "weight management", "skin health"],
            "serving_suggestion": "1/4 to 1/2 of a medium avocado"
        },
        "blueberries": {
            "category": "fruit",
            "dietary_tags": ["vegetarian", "vegan", "plant_based", "paleo"],
            "allergies": [],
            "nutrients": ["antioxidants", "vitamin C", "fiber"],
            "benefits": ["brain health", "heart health", "anti-aging"],
            "serving_suggestion": "1/2 cup fresh or frozen"
        },
        "almonds": {
            "category": "nuts",
            "dietary_tags": ["vegetarian", "vegan", "plant_based", "keto", "paleo"],
            "allergies": ["nuts", "tree nuts"],
            "nutrients": ["healthy fats", "protein", "vitamin E", "magnesium"],
            "benefits": ["heart health", "weight management", "blood sugar control"],
            "serving_suggestion": "1/4 cup (about 23 almonds)"
        },
        "quinoa": {
            "category": "grain",
            "dietary_tags": ["vegetarian", "vegan", "plant_based", "gluten_free"],
            "allergies": [],
            "nutrients": ["protein", "fiber", "magnesium", "iron"],
            "benefits": ["muscle building", "digestive health", "energy production"],
            "serving_suggestion": "1/2 cup cooked as a side dish or in salads"
        },
        "greek yogurt": {
            "category": "dairy",
            "dietary_tags": ["high_protein", "probiotic"],
            "allergies": ["dairy", "milk"],
            "nutrients": ["protein", "calcium", "probiotics", "vitamin B12"],
            "benefits": ["gut health", "bone health", "muscle recovery"],
            "serving_suggestion": "1 cup plain, with fruit or as a base for smoothies"
        }
    }
    
    # Filter foods based on dietary preferences, allergies, and health goals
    recommended_foods = []
    
    for food_name, food_info in food_database.items():
        # Skip if the food contains an allergen
        if any(allergy in food_info["allergies"] for allergy in allergies):
            continue
        
        # Check dietary preferences
        if dietary_preferences:
            matches_preference = False
            for pref in dietary_preferences:
                # Special handling for common dietary patterns
                if pref == "vegetarian" and "vegetarian" in food_info["dietary_tags"]:
                    matches_preference = True
                    break
                elif pref == "vegan" and "vegan" in food_info["dietary_tags"]:
                    matches_preference = True
                    break
                elif pref == "keto" and "keto" in food_info["dietary_tags"]:
                    matches_preference = True
                    break
                elif pref == "paleo" and "paleo" in food_info["dietary_tags"]:
                    matches_preference = True
                    break
                elif pref == "gluten free" and "gluten_free" in food_info["dietary_tags"]:
                    matches_preference = True
                    break
                elif pref in food_info["dietary_tags"]:
                    matches_preference = True
                    break
            
            if not matches_preference:
                continue
        
        # Check for nutrient focus
        if nutrient_focus and nutrient_focus not in [n.lower() for n in food_info["nutrients"]]:
            continue
        
        # Check health goals
        if health_goals:
            matches_goal = False
            for goal in health_goals:
                if any(goal in benefit.lower() for benefit in food_info["benefits"]):
                    matches_goal = True
                    break
            
            if not matches_goal:
                continue
        
        # Add to recommendations if it passed all filters
        recommended_foods.append({
            "food": food_name,
            "category": food_info["category"],
            "benefits": food_info["benefits"],
            "nutrients": food_info["nutrients"],
            "serving_suggestion": food_info["serving_suggestion"]
        })
    
    # Return the results
    if recommended_foods:
        return {
            "status": "success",
            "recommendations": recommended_foods
        }
    else:
        return {
            "status": "error",
            "error_message": "No foods match the specified criteria. Try broadening your preferences or reducing restrictions."
        }

# Create the Function Tool
food_recommendation_tool = FunctionTool(func=recommend_foods) 