from google.adk.tools import FunctionTool
from typing import Dict, List, Optional

def analyze_diet(food_log: List[Dict]) -> Dict:
    """Analyzes a user's diet based on their food log and provides nutritional insights.
    
    Use this tool when the user wants to analyze their diet, identify nutritional
    gaps or excesses, or get feedback on their eating patterns.
    
    Args:
        food_log: A list of dictionaries representing the user's food intake, each containing:
            {
                "food": name of the food consumed (e.g., "apple", "chicken breast"),
                "quantity": amount of the food (e.g., 100),
                "unit": unit of measurement (e.g., "g", "oz", "cup", "piece"),
                "meal_type": type of meal (e.g., "breakfast", "lunch", "dinner", "snack"),
                "time": time of consumption (optional)
            }
    
    Returns:
        A dictionary with the following structure:
        {
            "status": "success" or "error",
            "total_calories": total calories consumed,
            "macronutrient_distribution": {
                "protein_percent": percentage of calories from protein,
                "carbohydrates_percent": percentage of calories from carbs,
                "fat_percent": percentage of calories from fat
            },
            "nutritional_analysis": {
                "strengths": list of nutritional strengths in the diet,
                "gaps": list of potential nutritional gaps,
                "recommendations": list of suggestions for improvement
            },
            "meal_pattern_analysis": analysis of meal timing and distribution,
            "error_message": description of error (only if status is "error")
        }
    """
    # In a real implementation, this would use a comprehensive nutritional analysis system
    # For demonstration, we'll use a simplified approach with mock data
    
    # Food database with nutritional information
    food_database = {
        "apple": {
            "calories": 52,
            "protein": 0.3,
            "carbohydrates": 13.8,
            "fat": 0.2,
            "fiber": 2.4,
            "vitamins": ["vitamin C"],
            "minerals": ["potassium"],
            "food_group": "fruit"
        },
        "banana": {
            "calories": 89,
            "protein": 1.1,
            "carbohydrates": 22.8,
            "fat": 0.3,
            "fiber": 2.6,
            "vitamins": ["vitamin C", "vitamin B6"],
            "minerals": ["potassium", "magnesium"],
            "food_group": "fruit"
        },
        "chicken breast": {
            "calories": 165,
            "protein": 31,
            "carbohydrates": 0,
            "fat": 3.6,
            "fiber": 0,
            "vitamins": ["vitamin B6", "niacin"],
            "minerals": ["phosphorus", "selenium"],
            "food_group": "protein"
        },
        "salmon": {
            "calories": 206,
            "protein": 22,
            "carbohydrates": 0,
            "fat": 13,
            "fiber": 0,
            "vitamins": ["vitamin D", "vitamin B12"],
            "minerals": ["selenium", "phosphorus"],
            "food_group": "protein"
        },
        "broccoli": {
            "calories": 34,
            "protein": 2.8,
            "carbohydrates": 6.6,
            "fat": 0.4,
            "fiber": 2.6,
            "vitamins": ["vitamin C", "vitamin K", "folate"],
            "minerals": ["potassium", "calcium"],
            "food_group": "vegetable"
        },
        "spinach": {
            "calories": 23,
            "protein": 2.9,
            "carbohydrates": 3.6,
            "fat": 0.4,
            "fiber": 2.2,
            "vitamins": ["vitamin A", "vitamin K", "folate"],
            "minerals": ["iron", "calcium"],
            "food_group": "vegetable"
        },
        "brown rice": {
            "calories": 112,
            "protein": 2.6,
            "carbohydrates": 23.5,
            "fat": 0.9,
            "fiber": 1.8,
            "vitamins": ["niacin", "vitamin B6"],
            "minerals": ["magnesium", "phosphorus"],
            "food_group": "grain"
        },
        "white bread": {
            "calories": 74,
            "protein": 2.6,
            "carbohydrates": 13.8,
            "fat": 1,
            "fiber": 0.8,
            "vitamins": ["thiamin", "folate"],
            "minerals": ["calcium", "iron"],
            "food_group": "grain"
        },
        "greek yogurt": {
            "calories": 59,
            "protein": 10,
            "carbohydrates": 3.6,
            "fat": 0.4,
            "fiber": 0,
            "vitamins": ["vitamin B12", "riboflavin"],
            "minerals": ["calcium", "phosphorus"],
            "food_group": "dairy"
        },
        "almonds": {
            "calories": 164,
            "protein": 6,
            "carbohydrates": 6,
            "fat": 14,
            "fiber": 3.5,
            "vitamins": ["vitamin E", "riboflavin"],
            "minerals": ["magnesium", "phosphorus"],
            "food_group": "nuts"
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
    
    # Initialize counters
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0
    total_fiber = 0
    
    # Track food groups and nutrients
    food_groups = {
        "fruit": 0,
        "vegetable": 0,
        "protein": 0,
        "grain": 0,
        "dairy": 0,
        "nuts": 0
    }
    
    vitamins_consumed = set()
    minerals_consumed = set()
    
    # Track meal patterns
    meals = {
        "breakfast": 0,
        "lunch": 0,
        "dinner": 0,
        "snack": 0
    }
    
    # Items not found in the database
    items_not_found = []
    
    # Process each food item in the log
    for item in food_log:
        food_name = item["food"].lower()
        quantity = item["quantity"]
        unit = item["unit"].lower()
        meal_type = item["meal_type"].lower() if "meal_type" in item else "snack"
        
        # Update meal count
        if meal_type in meals:
            meals[meal_type] += 1
        
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
                # Default to assuming the unit is grams
                quantity_in_grams = quantity
            
            # Calculate scaling factor
            scaling_factor = quantity_in_grams / 100  # Assuming database values are per 100g
            
            # Add to totals
            food_data = food_database[food_name]
            total_calories += food_data["calories"] * scaling_factor
            total_protein += food_data["protein"] * scaling_factor
            total_carbohydrates += food_data["carbohydrates"] * scaling_factor
            total_fat += food_data["fat"] * scaling_factor
            total_fiber += food_data["fiber"] * scaling_factor
            
            # Update food group count
            if "food_group" in food_data and food_data["food_group"] in food_groups:
                food_groups[food_data["food_group"]] += 1
            
            # Update vitamins and minerals
            for vitamin in food_data["vitamins"]:
                vitamins_consumed.add(vitamin)
            
            for mineral in food_data["minerals"]:
                minerals_consumed.add(mineral)
        else:
            items_not_found.append(food_name)
    
    # Calculate macronutrient distribution (calories)
    protein_calories = total_protein * 4  # 4 calories per gram of protein
    carb_calories = total_carbohydrates * 4  # 4 calories per gram of carbs
    fat_calories = total_fat * 9  # 9 calories per gram of fat
    
    total_macro_calories = protein_calories + carb_calories + fat_calories
    
    # Avoid division by zero
    if total_macro_calories > 0:
        protein_percent = round((protein_calories / total_macro_calories) * 100, 1)
        carb_percent = round((carb_calories / total_macro_calories) * 100, 1)
        fat_percent = round((fat_calories / total_macro_calories) * 100, 1)
    else:
        protein_percent = 0
        carb_percent = 0
        fat_percent = 0
    
    # Analyze diet strengths and gaps
    strengths = []
    gaps = []
    recommendations = []
    
    # Check protein intake
    if protein_percent >= 15:
        strengths.append("Adequate protein intake")
    else:
        gaps.append("Low protein intake")
        recommendations.append("Consider adding more lean protein sources like chicken, fish, tofu, or legumes")
    
    # Check fiber intake
    if total_fiber >= 25:
        strengths.append("Good fiber intake")
    else:
        gaps.append("Low fiber intake")
        recommendations.append("Increase consumption of fruits, vegetables, and whole grains")
    
    # Check food group diversity
    if food_groups["fruit"] >= 2:
        strengths.append("Good fruit consumption")
    else:
        gaps.append("Low fruit intake")
        recommendations.append("Try to include more fruits in your diet")
    
    if food_groups["vegetable"] >= 3:
        strengths.append("Good vegetable consumption")
    else:
        gaps.append("Low vegetable intake")
        recommendations.append("Add more vegetables to your meals")
    
    # Check meal patterns
    meal_pattern_analysis = ""
    if meals["breakfast"] == 0:
        meal_pattern_analysis += "You skipped breakfast. "
        recommendations.append("Consider eating breakfast to kickstart your metabolism")
    
    if sum(meals.values()) > 5:
        meal_pattern_analysis += "You're eating frequently throughout the day. "
    elif sum(meals.values()) < 3:
        meal_pattern_analysis += "You're not eating enough meals/snacks throughout the day. "
        recommendations.append("Try to maintain regular meal times")
    else:
        meal_pattern_analysis += "You have a good meal frequency. "
    
    # Prepare the result
    if len(food_log) > 0:
        return {
            "status": "success",
            "total_calories": round(total_calories, 1),
            "macronutrient_distribution": {
                "protein_percent": protein_percent,
                "carbohydrates_percent": carb_percent,
                "fat_percent": fat_percent
            },
            "nutritional_analysis": {
                "strengths": strengths,
                "gaps": gaps,
                "recommendations": recommendations
            },
            "meal_pattern_analysis": meal_pattern_analysis,
            "items_not_found": items_not_found
        }
    else:
        return {
            "status": "error",
            "error_message": "No food items provided for analysis."
        }

# Create the Function Tool
diet_analysis_tool = FunctionTool(func=analyze_diet) 