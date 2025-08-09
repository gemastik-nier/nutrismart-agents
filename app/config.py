"""
Configuration settings for the NutriAgent application.
"""

import os

# Google AI API configuration
# Replace this with your actual API key or set it as an environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY_HERE")

# Model configuration
MODEL_ID = os.getenv("MODEL_ID", "gemini-2.0-flash")

# Backend base URL for external API calls (personal agent, latest nutrition facts)
# Example: https://api.your-backend.com
BE_URL = os.getenv("BE_URL", "http://localhost:8000")