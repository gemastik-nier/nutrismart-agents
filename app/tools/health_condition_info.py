from google.adk.tools import FunctionTool
from typing import Dict, List, Optional

def get_health_condition_info(condition: str) -> Dict:
    """Provides information about nutrition-related health conditions.
    
    Use this tool when the user asks about health conditions related to nutrition,
    such as diabetes, hypertension, celiac disease, or food allergies. This tool
    provides general information about the condition and nutritional considerations,
    but does NOT provide medical advice.
    
    Args:
        condition: The health condition to get information about (e.g., "diabetes", "hypertension", "celiac disease")
    
    Returns:
        A dictionary with the following structure:
        {
            "status": "success" or "error",
            "condition_name": the standardized name of the condition,
            "description": general description of the condition,
            "nutritional_considerations": list of nutritional considerations for the condition,
            "foods_to_include": list of foods that may be beneficial,
            "foods_to_limit": list of foods that may be best to limit or avoid,
            "disclaimer": medical disclaimer,
            "error_message": description of error (only if status is "error")
        }
    """
    # In a real implementation, this would query a medical database or API
    # For demonstration, we'll use a simplified approach with information for common conditions
    
    # Normalize the condition name
    condition_lower = condition.lower()
    
    # Database of health conditions
    health_conditions = {
        "diabetes": {
            "condition_name": "Diabetes",
            "description": "Diabetes is a chronic condition characterized by high levels of glucose in the blood due to the body's inability to produce or effectively use insulin. There are several types, with Type 1 and Type 2 being the most common.",
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
            ]
        },
        "hypertension": {
            "condition_name": "Hypertension (High Blood Pressure)",
            "description": "Hypertension is a condition in which the force of blood against artery walls is consistently too high, which can lead to heart disease, stroke, and other health problems if not controlled.",
            "nutritional_considerations": [
                "Reduce sodium (salt) intake to help lower blood pressure",
                "Maintain a healthy weight through balanced nutrition",
                "Consider the DASH (Dietary Approaches to Stop Hypertension) eating plan",
                "Limit alcohol consumption",
                "Ensure adequate potassium, magnesium, and calcium intake"
            ],
            "foods_to_include": [
                "Fruits and vegetables (especially those high in potassium like bananas, oranges, potatoes)",
                "Low-fat dairy products (good source of calcium)",
                "Whole grains (oats, brown rice, whole wheat)",
                "Lean proteins (fish, especially fatty fish with omega-3s)",
                "Nuts, seeds, and legumes"
            ],
            "foods_to_limit": [
                "High-sodium foods (processed foods, canned soups, deli meats)",
                "Salty snacks (chips, pretzels, salted nuts)",
                "Foods high in saturated and trans fats",
                "Excessive caffeine",
                "Alcohol"
            ]
        },
        "celiac disease": {
            "condition_name": "Celiac Disease",
            "description": "Celiac disease is an autoimmune disorder where ingestion of gluten leads to damage in the small intestine. It affects people genetically predisposed to the condition and can cause both digestive and non-digestive symptoms.",
            "nutritional_considerations": [
                "Strict avoidance of gluten is essential (found in wheat, barley, and rye)",
                "Focus on naturally gluten-free whole foods",
                "Be vigilant about cross-contamination",
                "Monitor for nutritional deficiencies common in celiac disease (iron, B vitamins, calcium, vitamin D)",
                "Choose gluten-free grains and starches"
            ],
            "foods_to_include": [
                "Gluten-free grains and starches (rice, corn, quinoa, buckwheat, certified gluten-free oats)",
                "Fresh fruits and vegetables",
                "Lean proteins (meat, fish, eggs, legumes)",
                "Dairy products (if tolerated)",
                "Nuts and seeds"
            ],
            "foods_to_limit": [
                "All foods containing wheat, barley, and rye",
                "Most conventional breads, pastas, cereals, and baked goods",
                "Many processed foods that may contain hidden gluten",
                "Beer and some alcoholic beverages",
                "Sauces and condiments that may contain gluten (soy sauce, some salad dressings)"
            ]
        },
        "irritable bowel syndrome": {
            "condition_name": "Irritable Bowel Syndrome (IBS)",
            "description": "IBS is a common disorder affecting the large intestine, characterized by symptoms like cramping, abdominal pain, bloating, gas, and diarrhea or constipation. It's a chronic condition that requires long-term management.",
            "nutritional_considerations": [
                "Identify and avoid personal trigger foods",
                "Consider a low FODMAP diet under professional guidance",
                "Stay well-hydrated with water",
                "Eat smaller, more frequent meals",
                "Increase soluble fiber intake gradually if constipation is predominant"
            ],
            "foods_to_include": [
                "Low FODMAP fruits (e.g., bananas, blueberries, oranges, strawberries)",
                "Low FODMAP vegetables (e.g., carrots, cucumber, eggplant, lettuce)",
                "Lactose-free dairy (if dairy is a trigger)",
                "Lean proteins",
                "Gluten-free grains (if gluten sensitivity is present)"
            ],
            "foods_to_limit": [
                "High FODMAP foods (varies by individual)",
                "Gas-producing foods (e.g., beans, lentils, cabbage, onions)",
                "Caffeine and alcohol",
                "Fatty or fried foods",
                "Artificial sweeteners (especially sorbitol, mannitol)"
            ]
        },
        "gout": {
            "condition_name": "Gout",
            "description": "Gout is a type of inflammatory arthritis characterized by sudden, severe attacks of pain, swelling, redness and tenderness in joints, often at the base of the big toe. It occurs when urate crystals accumulate in joints due to high levels of uric acid in the blood.",
            "nutritional_considerations": [
                "Limit foods high in purines, which are broken down into uric acid",
                "Stay well-hydrated to help flush uric acid from the body",
                "Maintain a healthy weight (weight loss can help reduce uric acid levels)",
                "Limit alcohol consumption, especially beer",
                "Consider a Mediterranean-style diet"
            ],
            "foods_to_include": [
                "Low-fat dairy products (may help lower uric acid levels)",
                "Plant proteins (tofu, legumes in moderation)",
                "Whole grains",
                "Fruits (especially cherries, which may have anti-inflammatory properties)",
                "Vegetables (except those high in purines)"
            ],
            "foods_to_limit": [
                "Organ meats (liver, kidneys, sweetbreads)",
                "Seafood high in purines (anchovies, sardines, mussels, scallops)",
                "Red meat and game meats",
                "Alcohol (especially beer)",
                "High-fructose corn syrup"
            ]
        },
        "food allergies": {
            "condition_name": "Food Allergies",
            "description": "Food allergies are immune system reactions that occur soon after eating a certain food. Even a tiny amount of the allergy-causing food can trigger signs and symptoms such as digestive problems, hives, or swollen airways.",
            "nutritional_considerations": [
                "Strict avoidance of allergens is essential",
                "Read food labels carefully to identify hidden allergens",
                "Be aware of cross-contamination risks",
                "Ensure nutritional adequacy when eliminating food groups",
                "Consider working with a registered dietitian to develop a safe, balanced diet"
            ],
            "foods_to_include": [
                "A wide variety of non-allergenic foods",
                "Nutrient-dense alternatives to replace excluded foods",
                "Foods rich in nutrients commonly found in excluded food groups",
                "Fresh, whole foods with simple ingredients",
                "Fortified foods if needed to meet nutritional needs"
            ],
            "foods_to_limit": [
                "Known allergens (common ones include milk, eggs, peanuts, tree nuts, wheat, soy, fish, and shellfish)",
                "Processed foods that may contain hidden allergens",
                "Foods at high risk for cross-contamination",
                "Restaurant meals without clear allergen information",
                "Packaged foods with unclear labeling"
            ]
        },
        "lactose intolerance": {
            "condition_name": "Lactose Intolerance",
            "description": "Lactose intolerance is a digestive disorder caused by the inability to digest lactose, the main carbohydrate in dairy products. It results from a deficiency of lactase, the enzyme produced in the small intestine that breaks down lactose.",
            "nutritional_considerations": [
                "Limit or avoid lactose-containing foods based on personal tolerance",
                "Ensure adequate calcium and vitamin D intake from non-dairy sources or supplements",
                "Consider lactose-free dairy products",
                "Try consuming small amounts of dairy with meals",
                "Use lactase enzyme supplements when consuming dairy"
            ],
            "foods_to_include": [
                "Lactose-free milk and dairy products",
                "Plant-based milk alternatives (soy, almond, oat) fortified with calcium and vitamin D",
                "Hard, aged cheeses (naturally lower in lactose)",
                "Yogurt with live active cultures (may be better tolerated)",
                "Non-dairy calcium sources (leafy greens, fortified foods, canned fish with bones)"
            ],
            "foods_to_limit": [
                "Milk and cream",
                "Ice cream and soft cheeses",
                "Processed foods containing milk ingredients",
                "Whey protein supplements",
                "Some baked goods and desserts"
            ]
        }
    }
    
    # Check for condition in database
    for key, info in health_conditions.items():
        if key in condition_lower or condition_lower in key:
            # Add disclaimer to all responses
            info["disclaimer"] = "IMPORTANT: This information is for educational purposes only and is not intended as medical advice. Always consult with healthcare professionals for diagnosis, treatment, and personalized dietary recommendations."
            info["status"] = "success"
            return info
    
    # If condition not found
    return {
        "status": "error",
        "error_message": f"Information about '{condition}' is not available. Please try a different condition or consult a healthcare professional.",
        "disclaimer": "This tool provides general information about common nutrition-related health conditions but is not a substitute for professional medical advice, diagnosis, or treatment."
    }

# Create the Function Tool
health_condition_info_tool = FunctionTool(func=get_health_condition_info) 