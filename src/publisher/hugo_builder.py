import os
import datetime
import logging
import re

logger = logging.getLogger(__name__)

class HugoBuilder:
    def __init__(self, content_dir="blog/content/posts"):
        self.content_dir = content_dir
        os.makedirs(self.content_dir, exist_ok=True)

    def _sanitize_filename(self, title):
        # Remove invalid characters and truncate
        filename = re.sub(r'[\\/*?:"<>|]', "", title)
        return filename[:50].replace(" ", "_")

    def save_article(self, title, content, tags=None):
        """Save the article as a Hugo Markdown file."""
        if tags is None:
            tags = ["AI", "SideHustle"]
        
        date_str = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')
        filename = f"{self._sanitize_filename(title)}.md"
        filepath = os.path.join(self.content_dir, filename)

        # Create Front Matter
        front_matter = f"""---
title: "{title}"
date: {date_str}
draft: false
tags: {tags}
categories: ["Money"]
---
"""
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(front_matter + "\n")
                f.write(content)
            logger.info(f"Article saved to {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"Error saving article: {e}")
            return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    builder = HugoBuilder()
    builder.save_article("Test Article Title", "# Hello World\nThis is a test.")
