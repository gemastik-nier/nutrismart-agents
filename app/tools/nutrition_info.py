from google.adk.tools import FunctionTool
from typing import Dict, Optional, List

def get_nutrition_info(food_name: str, quantity: float = 100.0, unit: str = "g") -> Dict:
    """Retrieves nutritional information for a specified food.
    
    Use this tool when the user asks about nutritional content, vitamins, minerals,
    or general nutrition information about a specific food. This tool queries a nutrition
    database to provide accurate information.
    
    Args:
        food_name: The name of the food to look up (e.g., "apple", "chicken breast", "quinoa")
        quantity: The amount of food (default is 100.0)
        unit: The unit of measurement (e.g., "g" for grams, "oz" for ounces, "cup", "piece")
        
    Returns:
        A dictionary containing nutritional information with the following structure:
        {
            "status": "success" or "error",
            "food_name": the normalized food name,
            "quantity": the quantity used for calculation,
            "unit": the unit used for calculation,
            "calories": number of calories,
            "macronutrients": {
                "protein": protein in grams,
                "carbohydrates": carbohydrates in grams,
                "fat": fat in grams,
                "fiber": fiber in grams
            },
            "micronutrients": {
                "vitamin_a": amount in appropriate units,
                "vitamin_c": amount in appropriate units,
                # other vitamins and minerals
            },
            "error_message": description of error (only if status is "error")
        }
    """
    # In a real implementation, this would query a nutrition database API
    # For demonstration, we'll return mock data for a few common foods
    
    food_database = {
        "apple": {
            "calories": 52,
            "macronutrients": {
                "protein": 0.3,
                "carbohydrates": 13.8,
                "fat": 0.2,
                "fiber": 2.4
            },
            "micronutrients": {
                "vitamin_c": "4.6 mg",
                "potassium": "107 mg"
            }
        },
        "banana": {
            "calories": 89,
            "macronutrients": {
                "protein": 1.1,
                "carbohydrates": 22.8,
                "fat": 0.3,
                "fiber": 2.6
            },
            "micronutrients": {
                "vitamin_c": "8.7 mg",
                "potassium": "358 mg"
            }
        },
        "chicken breast": {
            "calories": 165,
            "macronutrients": {
                "protein": 31,
                "carbohydrates": 0,
                "fat": 3.6,
                "fiber": 0
            },
            "micronutrients": {
                "vitamin_b6": "0.6 mg",
                "niacin": "13.7 mg"
            }
        }
    }
    
    food_name_lower = food_name.lower()
    
    # Calculate scaling factor based on quantity and unit
    scaling_factor = quantity / 100.0  # Default is per 100g
    
    # Different scaling for different units (simplified)
    if unit == "oz":
        scaling_factor = quantity * 0.28  # 1 oz ≈ 28g
    elif unit == "cup":
        # Rough approximation - would be different for different foods
        scaling_factor = quantity * 2.4  # Assuming 1 cup ≈ 240g
    elif unit == "piece" and food_name_lower in ["apple", "banana"]:
        # Rough approximation for a medium piece
        scaling_factor = quantity * 1.2  # Assuming 1 piece ≈ 120g
    
    if food_name_lower in food_database:
        food_data = food_database[food_name_lower]
        
        # Scale the nutritional values
        scaled_data = {
            "status": "success",
            "food_name": food_name,
            "quantity": quantity,
            "unit": unit,
            "calories": round(food_data["calories"] * scaling_factor, 1),
            "macronutrients": {
                nutrient: round(value * scaling_factor, 1) 
                for nutrient, value in food_data["macronutrients"].items()
            },
            "micronutrients": food_data["micronutrients"]  # Not scaling micronutrients for simplicity
        }
        
        return scaled_data
    else:
        return {
            "status": "error",
            "error_message": f"Nutritional information for '{food_name}' not found in database."
        }

# Create the Function Tool
nutrition_info_tool = FunctionTool(func=get_nutrition_info) 