from google.adk.tools import FunctionTool
from typing import Dict, Optional

def convert_measurement(
    food: str,
    amount: float,
    from_unit: str,
    to_unit: str
) -> Dict:
    """Converts food measurements from one unit to another.
    
    Use this tool when the user needs to convert between different units of measurement
    for food ingredients, such as converting cups to grams, teaspoons to tablespoons,
    or ounces to milliliters.
    
    Args:
        food: The food item being measured (e.g., "flour", "sugar", "milk")
        amount: The numerical amount to convert
        from_unit: The unit to convert from (e.g., "cup", "tbsp", "oz", "g")
        to_unit: The unit to convert to (e.g., "g", "ml", "tsp", "cup")
    
    Returns:
        A dictionary with the following structure:
        {
            "status": "success" or "error",
            "food": the food item,
            "original_amount": the original amount,
            "original_unit": the original unit,
            "converted_amount": the converted amount,
            "converted_unit": the converted unit,
            "error_message": description of error (only if status is "error")
        }
    """
    # In a real implementation, this would use a comprehensive food measurement database
    # For demonstration, we'll use a simplified approach with common conversions
    
    # Normalize units to standard abbreviations
    unit_mapping = {
        # Volume units
        "cup": "cup",
        "cups": "cup",
        "c": "cup",
        "tablespoon": "tbsp",
        "tablespoons": "tbsp",
        "tbsp": "tbsp",
        "tb": "tbsp",
        "teaspoon": "tsp",
        "teaspoons": "tsp",
        "tsp": "tsp",
        "fluid ounce": "fl oz",
        "fluid ounces": "fl oz",
        "fl oz": "fl oz",
        "floz": "fl oz",
        "milliliter": "ml",
        "milliliters": "ml",
        "ml": "ml",
        "liter": "l",
        "liters": "l",
        "l": "l",
        "pint": "pint",
        "pints": "pint",
        "pt": "pint",
        "quart": "quart",
        "quarts": "quart",
        "qt": "quart",
        "gallon": "gallon",
        "gallons": "gallon",
        "gal": "gallon",
        
        # Weight units
        "gram": "g",
        "grams": "g",
        "g": "g",
        "kilogram": "kg",
        "kilograms": "kg",
        "kg": "kg",
        "ounce": "oz",
        "ounces": "oz",
        "oz": "oz",
        "pound": "lb",
        "pounds": "lb",
        "lb": "lb",
        "lbs": "lb",
        
        # Count units
        "piece": "piece",
        "pieces": "piece",
        "slice": "slice",
        "slices": "slice"
    }
    
    # Normalize input units
    from_unit_norm = from_unit.lower()
    to_unit_norm = to_unit.lower()
    
    if from_unit_norm in unit_mapping:
        from_unit_norm = unit_mapping[from_unit_norm]
    else:
        return {
            "status": "error",
            "error_message": f"Unknown source unit: '{from_unit}'"
        }
    
    if to_unit_norm in unit_mapping:
        to_unit_norm = unit_mapping[to_unit_norm]
    else:
        return {
            "status": "error",
            "error_message": f"Unknown target unit: '{to_unit}'"
        }
    
    # Check if units are in the same category
    volume_units = ["cup", "tbsp", "tsp", "fl oz", "ml", "l", "pint", "quart", "gallon"]
    weight_units = ["g", "kg", "oz", "lb"]
    count_units = ["piece", "slice"]
    
    # Determine if we're converting between volume, weight, or count units
    same_category = False
    if from_unit_norm in volume_units and to_unit_norm in volume_units:
        same_category = True
        category = "volume"
    elif from_unit_norm in weight_units and to_unit_norm in weight_units:
        same_category = True
        category = "weight"
    elif from_unit_norm in count_units and to_unit_norm in count_units:
        same_category = True
        category = "count"
    
    # If not in the same category, we need density information for the food
    food_densities = {
        # Approximate densities in g/ml
        "flour": 0.53,
        "sugar": 0.85,
        "brown sugar": 0.72,
        "powdered sugar": 0.56,
        "salt": 1.2,
        "butter": 0.96,
        "oil": 0.92,
        "milk": 1.03,
        "water": 1.0,
        "honey": 1.42,
        "maple syrup": 1.32,
        "rice": 0.75,
        "oats": 0.4,
        "yogurt": 1.03
    }
    
    # Conversion factors within the same category
    volume_conversions = {
        "cup": {
            "cup": 1,
            "tbsp": 16,
            "tsp": 48,
            "fl oz": 8,
            "ml": 236.588,
            "l": 0.236588,
            "pint": 0.5,
            "quart": 0.25,
            "gallon": 0.0625
        },
        "tbsp": {
            "cup": 0.0625,
            "tbsp": 1,
            "tsp": 3,
            "fl oz": 0.5,
            "ml": 14.7868,
            "l": 0.0147868,
            "pint": 0.03125,
            "quart": 0.015625,
            "gallon": 0.00390625
        },
        "tsp": {
            "cup": 0.0208333,
            "tbsp": 0.333333,
            "tsp": 1,
            "fl oz": 0.166667,
            "ml": 4.92892,
            "l": 0.00492892,
            "pint": 0.0104167,
            "quart": 0.00520833,
            "gallon": 0.00130208
        },
        "fl oz": {
            "cup": 0.125,
            "tbsp": 2,
            "tsp": 6,
            "fl oz": 1,
            "ml": 29.5735,
            "l": 0.0295735,
            "pint": 0.0625,
            "quart": 0.03125,
            "gallon": 0.0078125
        },
        "ml": {
            "cup": 0.00422675,
            "tbsp": 0.067628,
            "tsp": 0.202884,
            "fl oz": 0.033814,
            "ml": 1,
            "l": 0.001,
            "pint": 0.00211338,
            "quart": 0.00105669,
            "gallon": 0.000264172
        },
        "l": {
            "cup": 4.22675,
            "tbsp": 67.628,
            "tsp": 202.884,
            "fl oz": 33.814,
            "ml": 1000,
            "l": 1,
            "pint": 2.11338,
            "quart": 1.05669,
            "gallon": 0.264172
        },
        "pint": {
            "cup": 2,
            "tbsp": 32,
            "tsp": 96,
            "fl oz": 16,
            "ml": 473.176,
            "l": 0.473176,
            "pint": 1,
            "quart": 0.5,
            "gallon": 0.125
        },
        "quart": {
            "cup": 4,
            "tbsp": 64,
            "tsp": 192,
            "fl oz": 32,
            "ml": 946.353,
            "l": 0.946353,
            "pint": 2,
            "quart": 1,
            "gallon": 0.25
        },
        "gallon": {
            "cup": 16,
            "tbsp": 256,
            "tsp": 768,
            "fl oz": 128,
            "ml": 3785.41,
            "l": 3.78541,
            "pint": 8,
            "quart": 4,
            "gallon": 1
        }
    }
    
    weight_conversions = {
        "g": {
            "g": 1,
            "kg": 0.001,
            "oz": 0.035274,
            "lb": 0.00220462
        },
        "kg": {
            "g": 1000,
            "kg": 1,
            "oz": 35.274,
            "lb": 2.20462
        },
        "oz": {
            "g": 28.3495,
            "kg": 0.0283495,
            "oz": 1,
            "lb": 0.0625
        },
        "lb": {
            "g": 453.592,
            "kg": 0.453592,
            "oz": 16,
            "lb": 1
        }
    }
    
    # Food-specific count to weight/volume conversions
    count_conversions = {
        "apple": {
            "piece": {
                "g": 180,  # Medium apple
                "cup": 1.5  # Chopped
            }
        },
        "banana": {
            "piece": {
                "g": 120,  # Medium banana
                "cup": 1  # Sliced
            }
        },
        "bread": {
            "slice": {
                "g": 30,  # Regular slice
                "oz": 1
            }
        },
        "egg": {
            "piece": {
                "g": 50,  # Medium egg without shell
                "cup": 0.25
            }
        }
    }
    
    # Perform the conversion
    if same_category:
        if category == "volume":
            converted_amount = amount * volume_conversions[from_unit_norm][to_unit_norm]
            return {
                "status": "success",
                "food": food,
                "original_amount": amount,
                "original_unit": from_unit,
                "converted_amount": round(converted_amount, 3),
                "converted_unit": to_unit
            }
        elif category == "weight":
            converted_amount = amount * weight_conversions[from_unit_norm][to_unit_norm]
            return {
                "status": "success",
                "food": food,
                "original_amount": amount,
                "original_unit": from_unit,
                "converted_amount": round(converted_amount, 3),
                "converted_unit": to_unit
            }
        elif category == "count":
            # Direct count conversion (e.g., 1 piece = 1 piece)
            if from_unit_norm == to_unit_norm:
                return {
                    "status": "success",
                    "food": food,
                    "original_amount": amount,
                    "original_unit": from_unit,
                    "converted_amount": amount,
                    "converted_unit": to_unit
                }
            else:
                return {
                    "status": "error",
                    "error_message": f"Cannot convert between different count units: {from_unit} to {to_unit}"
                }
    else:
        # Cross-category conversion (requires food density or specific conversion data)
        food_lower = food.lower()
        
        # Check if we have count conversion data for this food
        if from_unit_norm in count_units and food_lower in count_conversions and from_unit_norm in count_conversions[food_lower]:
            if to_unit_norm in count_conversions[food_lower][from_unit_norm]:
                # Direct conversion from count to target unit exists
                converted_amount = amount * count_conversions[food_lower][from_unit_norm][to_unit_norm]
                return {
                    "status": "success",
                    "food": food,
                    "original_amount": amount,
                    "original_unit": from_unit,
                    "converted_amount": round(converted_amount, 3),
                    "converted_unit": to_unit
                }
        
        # Check if we're converting between volume and weight
        if (from_unit_norm in volume_units and to_unit_norm in weight_units) or (from_unit_norm in weight_units and to_unit_norm in volume_units):
            # Need density information
            if food_lower in food_densities:
                density = food_densities[food_lower]  # g/ml
                
                # First convert to ml if from_unit is volume
                if from_unit_norm in volume_units:
                    amount_in_ml = amount * volume_conversions[from_unit_norm]["ml"]
                    amount_in_g = amount_in_ml * density
                    
                    # Then convert from g to target weight unit
                    if to_unit_norm in weight_units:
                        converted_amount = amount_in_g * weight_conversions["g"][to_unit_norm]
                    else:
                        return {
                            "status": "error",
                            "error_message": f"Unsupported conversion: {from_unit} to {to_unit}"
                        }
                
                # First convert to g if from_unit is weight
                elif from_unit_norm in weight_units:
                    amount_in_g = amount * weight_conversions[from_unit_norm]["g"]
                    amount_in_ml = amount_in_g / density
                    
                    # Then convert from ml to target volume unit
                    if to_unit_norm in volume_units:
                        converted_amount = amount_in_ml * volume_conversions["ml"][to_unit_norm]
                    else:
                        return {
                            "status": "error",
                            "error_message": f"Unsupported conversion: {from_unit} to {to_unit}"
                        }
                
                return {
                    "status": "success",
                    "food": food,
                    "original_amount": amount,
                    "original_unit": from_unit,
                    "converted_amount": round(converted_amount, 3),
                    "converted_unit": to_unit
                }
            else:
                return {
                    "status": "error",
                    "error_message": f"Density information for '{food}' is not available for conversion between {from_unit} and {to_unit}"
                }
        else:
            return {
                "status": "error",
                "error_message": f"Cannot convert between {from_unit} and {to_unit} for {food}"
            }

# Create the Function Tool
measurement_conversion_tool = FunctionTool(func=convert_measurement) 