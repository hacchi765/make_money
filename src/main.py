import logging
import argparse
import sys
from src.fetcher.google_trends import TrendFetcher
from src.generator.article import ArticleGenerator
from src.publisher.hugo_builder import HugoBuilder

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="AI Money Maker System")
    parser.add_argument("--mode", choices=["test", "run"], default="test", help="Execution mode")
    parser.add_argument("--count", type=int, default=1, help="Number of articles to generate")
    args = parser.parse_args()

    logger.info(f"Starting AI Money Maker System in {args.mode} mode...")

    try:
        # 1. Fetch Trends
        fetcher = TrendFetcher()
        trends = fetcher.fetch_daily_trends()
        
        if not trends:
            logger.warning("No trends found. Exiting.")
            return

        # 2. Initialize Generator & Builder
        generator = ArticleGenerator()
        builder = HugoBuilder()

        # 3. Process Trends
        processed_count = 0
        for trend in trends:
            if processed_count >= args.count:
                break
            
            logger.info(f"Processing trend: {trend}")
            
            # Generate Content
            article_content = generator.generate_article(trend)
            if not article_content:
                logger.error(f"Failed to generate article for {trend}")
                continue

            # Save to Hugo
            # Extract H1 title if possible, else use trend
            title = trend
            lines = article_content.split('\n')
            for line in lines:
                if line.startswith('# H1: ') or line.startswith('# '):
                    title = line.replace('# H1: ', '').replace('# ', '').strip()
                    break
            
            filepath = builder.save_article(title, article_content, tags=["Trend", "Money", "AI"])
            if filepath:
                logger.info(f"Successfully created article: {filepath}")
                processed_count += 1
            else:
                logger.error(f"Failed to save article for {trend}")

        logger.info(f"Completed processing. Generated {processed_count} articles.")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
