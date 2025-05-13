from google.adk.tools import FunctionTool
from typing import Dict, List, Optional

def calculate_nutrition(food_items: List[Dict]) -> Dict:
    """Calculates total calories and macronutrients for a list of food items.
    
    Use this tool when the user wants to know the nutritional content of a meal,
    recipe, or combination of foods. This tool aggregates nutritional information
    from multiple food items and provides a total.
    
    Args:
        food_items: A list of dictionaries, each containing:
            {
                "name": name of the food (e.g., "apple", "chicken breast"),
                "quantity": amount of the food (e.g., 100),
                "unit": unit of measurement (e.g., "g", "oz", "cup", "piece")
            }
    
    Returns:
        A dictionary with the following structure:
        {
            "status": "success" or "error",
            "total_calories": total calories for all items,
            "total_macronutrients": {
                "protein": total protein in grams,
                "carbohydrates": total carbohydrates in grams,
                "fat": total fat in grams,
                "fiber": total fiber in grams
            },
            "items_calculated": list of food items successfully calculated,
            "items_not_found": list of food items not found in the database,
            "error_message": description of error (only if status is "error")
        }
    """
    # In a real implementation, this would query a nutrition database API
    # For demonstration, we'll use a small mock database
    
    food_database = {
        "apple": {
            "base_quantity": 100,  # g
            "base_unit": "g",
            "calories": 52,
            "protein": 0.3,
            "carbohydrates": 13.8,
            "fat": 0.2,
            "fiber": 2.4
        },
        "banana": {
            "base_quantity": 100,
            "base_unit": "g",
            "calories": 89,
            "protein": 1.1,
            "carbohydrates": 22.8,
            "fat": 0.3,
            "fiber": 2.6
        },
        "chicken breast": {
            "base_quantity": 100,
            "base_unit": "g",
            "calories": 165,
            "protein": 31,
            "carbohydrates": 0,
            "fat": 3.6,
            "fiber": 0
        },
        "rice": {
            "base_quantity": 100,
            "base_unit": "g",
            "calories": 130,
            "protein": 2.7,
            "carbohydrates": 28,
            "fat": 0.3,
            "fiber": 0.4
        },
        "broccoli": {
            "base_quantity": 100,
            "base_unit": "g",
            "calories": 34,
            "protein": 2.8,
            "carbohydrates": 6.6,
            "fat": 0.4,
            "fiber": 2.6
        }
    }
    
    # Unit conversion factors (simplified)
    unit_conversions = {
        "g": 1,
        "oz": 28,  # 1 oz ≈ 28g
        "cup": {  # Approximate values, would be different for different foods
            "rice": 180,  # 1 cup of rice ≈ 180g
            "broccoli": 90,  # 1 cup of chopped broccoli ≈ 90g
            "default": 150  # Default assumption
        },
        "piece": {
            "apple": 180,  # 1 medium apple ≈ 180g
            "banana": 120,  # 1 medium banana ≈ 120g
            "default": 100  # Default assumption
        }
    }
    
    # Initialize totals
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0
    total_fiber = 0
    
    items_calculated = []
    items_not_found = []
    
    # Calculate nutrition for each food item
    for item in food_items:
        food_name = item["name"].lower()
        quantity = item["quantity"]
        unit = item["unit"].lower()
        
        if food_name in food_database:
            # Convert to grams based on unit
            if unit == "g":
                quantity_in_grams = quantity
            elif unit == "oz":
                quantity_in_grams = quantity * unit_conversions["oz"]
            elif unit == "cup":
                if food_name in unit_conversions["cup"]:
                    quantity_in_grams = quantity * unit_conversions["cup"][food_name]
                else:
                    quantity_in_grams = quantity * unit_conversions["cup"]["default"]
            elif unit == "piece":
                if food_name in unit_conversions["piece"]:
                    quantity_in_grams = quantity * unit_conversions["piece"][food_name]
                else:
                    quantity_in_grams = quantity * unit_conversions["piece"]["default"]
            else:
                # Default to assuming the unit is the same as the base unit
                quantity_in_grams = quantity
            
            # Calculate scaling factor
            scaling_factor = quantity_in_grams / food_database[food_name]["base_quantity"]
            
            # Add to totals
            food_data = food_database[food_name]
            total_calories += food_data["calories"] * scaling_factor
            total_protein += food_data["protein"] * scaling_factor
            total_carbohydrates += food_data["carbohydrates"] * scaling_factor
            total_fat += food_data["fat"] * scaling_factor
            total_fiber += food_data["fiber"] * scaling_factor
            
            items_calculated.append(food_name)
        else:
            items_not_found.append(food_name)
    
    # Prepare the result
    if len(items_calculated) > 0:
        return {
            "status": "success",
            "total_calories": round(total_calories, 1),
            "total_macronutrients": {
                "protein": round(total_protein, 1),
                "carbohydrates": round(total_carbohydrates, 1),
                "fat": round(total_fat, 1),
                "fiber": round(total_fiber, 1)
            },
            "items_calculated": items_calculated,
            "items_not_found": items_not_found
        }
    else:
        return {
            "status": "error",
            "error_message": "None of the provided food items were found in the database.",
            "items_not_found": items_not_found
        }

# Create the Function Tool
calorie_calculator_tool = FunctionTool(func=calculate_nutrition) 