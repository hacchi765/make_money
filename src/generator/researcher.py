import logging
from google import genai
from google.genai import types
from src.config import Config

logger = logging.getLogger(__name__)

class DeepResearchGenerator:
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        if not self.api_key:
            logger.warning("GEMINI_API_KEY not found in environment variables.")
        
        # Initialize the new Client
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = Config.GEMINI_RESEARCH_MODEL_NAME
        
        logger.info(f"Initialized DeepResearchGenerator with model: {self.model_name} and Google Search tool")

    def research_topic(self, keyword):
        """
        Research the given keyword using Google Search and generate a detailed report.
        """
        prompt = f"""
        You are a professional researcher. Your task is to gather comprehensive information about the topic: "{keyword}".
        
        Please use Google Search to find the latest and most relevant information.
        Focus on the following aspects:
        1. Definition and basic concepts.
        2. Current trends and statistics (2024-2025).
        3. Benefits and drawbacks/challenges.
        4. Specific actionable steps or methods related to the topic.
        5. Popular tools, services, or products commonly associated with this topic (for affiliate marketing context).
        6. Real-world examples or case studies if available.
        
        Output Format:
        Provide a detailed summary in Markdown format. 
        Cite sources where possible.
        The goal is to provide enough information for a writer to create a high-quality blog post without needing further research.
        """
        
        try:
            logger.info(f"Starting research for keyword: {keyword}...")
            
            # Using the new SDK's generate_content method
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(google_search=types.GoogleSearch())],
                    response_modalities=["TEXT"],
                    temperature=0.3,
                    max_output_tokens=8192,
                )
            )
            
            if response.text:
                logger.info("Research successful.")
                return response.text
            else:
                logger.warning("Research returned empty text.")
                return None
                
        except Exception as e:
            logger.error(f"Error during research: {e}")
            return None

if __name__ == "__main__":
    # Test script
    logging.basicConfig(level=logging.INFO)
    try:
        researcher = DeepResearchGenerator()
        result = researcher.research_topic("AI 副業 稼ぎ方")
        if result:
            print("\n--- Research Result ---\n")
            print(result)
        else:
            print("Research failed.")
    except Exception as e:
        print(f"Test execution failed: {e}")
