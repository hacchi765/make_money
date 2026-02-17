import google.generativeai as genai
from src.config import Config
import logging

logging.basicConfig(level=logging.INFO)

if not Config.GEMINI_API_KEY:
    print("No API Key found")
else:
    genai.configure(api_key=Config.GEMINI_API_KEY)
    print("Available models:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
