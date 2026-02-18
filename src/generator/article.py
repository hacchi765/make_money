import logging
import os
from google import genai
from google.genai import types
from src.config import Config
from src.generator.researcher import DeepResearchGenerator

logger = logging.getLogger(__name__)

class ArticleGenerator:
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        if not self.api_key:
            logger.warning("GEMINI_API_KEY not found in environment variables.")
        
        # Initialize the new Client
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = Config.GEMINI_WRITING_MODEL_NAME
        logger.info(f"Initialized ArticleGenerator with model: {self.model_name}")

    def generate_article(self, keyword, research_content=None):
        """Generate a blog article for the given keyword, optionally using research content."""
        
        research_context = ""
        if research_content:
            research_context = f"""
            以下は、このトピックに関する事前調査の結果です。
            この情報を最大限に活用し、具体的で信頼性の高い記事を作成してください。
            
            --- 調査結果 (Research Content) ---
            {research_content}
            -----------------------------------
            """

        prompt = f"""
        あなたは「AI×副業・投資」の専門家です。
        以下のキーワードについて、読者が知りたいことを網羅し、収益化（アフィリエイト誘導）を意識したブログ記事を作成してください。
        
        キーワード: {keyword}
        ターゲット: 副業や投資で稼ぎたい初心者
        
        {research_context}
        
        構成:
        1. 導入（読者の悩みに共感）
        2. {keyword}とは？（基礎知識）
        3. 稼ぐための具体的なステップ（Actionable Advice）
        4. おすすめのツール・サービス（ここにアフィリエイトリンクが入る想定で自然に誘導）
        5. まとめ
        
        条件:
        - タイトルは「H1: 」から始めてください。
        - 本文はMarkdown形式で出力してください。
        - 専門用語はわかりやすく解説してください。
        - 文字数は2000文字以上を目指してください。
        - 調査結果に含まれる具体的な数字や事例を積極的に盛り込んでください。
        """
        
        try:
            logger.info(f"Generating article for keyword: {keyword} (Research: {'Yes' if research_content else 'No'})...")
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    max_output_tokens=8192,
                )
            )
            
            if response.text:
                logger.info("Article generation successful.")
                return response.text
            else:
                logger.warning("Article generation returned empty text.")
                return None
                
        except Exception as e:
            logger.error(f"Error generating article: {e}")
            return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        if not Config.GEMINI_API_KEY:
            print("Please set GEMINI_API_KEY in .env to run this test.")
        else:
            # 1. Research Phase
            researcher = DeepResearchGenerator()
            print("Phase 1: Researching...")
            research_result = researcher.research_topic("AI 副業 稼ぎ方")
            
            if research_result:
                print("Research completed. Size:", len(research_result))
            else:
                print("Research failed or returned empty.")
                # Continue without research or abort depending on strategy. 
                # For test, we continue.

            # 2. Writing Phase
            generator = ArticleGenerator()
            print("Phase 2: Writing Article...")
            article = generator.generate_article("AI 動画生成 副業", research_content=research_result)
            
            if article:
                print("\n--- Generated Article ---\n")
                print(article[:500] + "...")
            else:
                print("Failed to generate article.")
    except Exception as e:
        print(f"Main execution failed: {e}")
