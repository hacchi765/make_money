import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    X_USERNAME = os.getenv("X_USERNAME")
    X_PASSWORD = os.getenv("X_PASSWORD")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    # Default model (keep for backward compatibility or general use)
    GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-2.0-flash")
    
    # Specific models for the hybrid workflow
    GEMINI_RESEARCH_MODEL_NAME = os.getenv("GEMINI_RESEARCH_MODEL_NAME", "models/gemini-2.5-flash")
    GEMINI_WRITING_MODEL_NAME = os.getenv("GEMINI_WRITING_MODEL_NAME", "models/gemini-2.5-flash")
    
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
