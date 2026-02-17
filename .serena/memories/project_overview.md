# AI Money Maker (Trend Blog Bot)

Automated system that fetches trending topics from Hatena, generates articles via Gemini 1.5 Flash, builds a static site with Hugo, and deploys it to Firebase Hosting.

## Tech
- **Python**: 3.11
- **AI**: Gemini 1.5 Flash (via `google-generativeai`)
- **SSG**: Hugo (Ananke)
- **Infra**: Cloud Run Jobs + Scheduler + Firebase Hosting + Artifact Registry.

## Key Features
- **Fetch Trends**: RSS feeds from Hatena Bookmark.
- **AI Content**: Prompts Gemini to write SEO articles with affiliate links.
- **Deploy**: Dockerized execution triggered 3x/day.
- **Cost**: Serverless architecture minimizes costs.

## Structure
- `src/`: Fetcher, Generator, Main Logic.
- `blog/`: Hugo site root.
- `scripts/`: Entrypoints.
- `.agent/workflows/`: Automation docs.
