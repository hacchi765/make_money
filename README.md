# AI Automated Money Making System (Phase 1)
"AI × Side Hustle/Investment" Trend Blog & SNS Automation System.

## Architecture
- **Content Engine**: Google Gemini 1.5 Pro
- **Trend Source**: Google Trends, Hatena, News API
- **Blog**: Hugo (Firebase Hosting)
- **SNS**: X Auto Poster (Playwright)

## Setup
1. Copy `.env.example` to `.env` and fill in secrets.
2. Install dependencies: `pip install -e .`
3. Install Playwright browsers: `playwright install`
4. Run Hugo: `hugo server -s blog`
