import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    X_USERNAME = os.getenv("X_USERNAME")
    X_PASSWORD = os.getenv("X_PASSWORD")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
