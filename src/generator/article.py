import os
import logging
import google.generativeai as genai
from src.config import Config

logger = logging.getLogger(__name__)

class ArticleGenerator:
    def __init__(self):
        api_key = Config.GEMINI_API_KEY
        if not api_key:
            logger.warning("GEMINI_API_KEY not found in environment variables.")
            # Fallback or error handling
            # raise ValueError("GEMINI_API_KEY is required.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        logger.info("Initialized Gemini API (google-generativeai).")

    def generate_article(self, keyword):
        """Generate a blog article for the given keyword."""
        prompt = f"""
        あなたは「AI×副業・投資」の専門家です。
        以下のキーワードについて、読者が知りたいことを網羅し、収益化（アフィリエイト誘導）を意識したブログ記事を作成してください。
        
        キーワード: {keyword}
        ターゲット: 副業や投資で稼ぎたい初心者
        
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
        """
        
        try:
            logger.info(f"Generating article for keyword: {keyword}...")
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    candidate_count=1,
                    max_output_tokens=8192,
                    temperature=0.7,
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
            generator = ArticleGenerator()
            article = generator.generate_article("AI 動画生成 副業")
            if article:
                print(article[:500] + "...")
            else:
                print("Failed to generate article.")
    except Exception as e:
        print(f"Main execution failed: {e}")
