import feedparser
import logging
import requests

logger = logging.getLogger(__name__)

class TrendFetcher:
    def __init__(self):
        # Hatena Bookmark IT Hotentry
        self.rss_url = "https://b.hatena.ne.jp/hotentry/it.rss"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def fetch_daily_trends(self):
        """Fetch daily trending topics from Hatena Bookmark."""
        try:
            logger.info(f"Fetching RSS feed from {self.rss_url}...")
            response = requests.get(self.rss_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            trends = []
            for entry in feed.entries:
                trends.append(entry.title)
            
            logger.info(f"Fetched {len(trends)} trends: {trends[:5]}...")
            return trends
        except Exception as e:
            logger.error(f"Error fetching trends: {e}")
            return []

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetcher = TrendFetcher()
    trends = fetcher.fetch_daily_trends()
    print(trends[:5])
