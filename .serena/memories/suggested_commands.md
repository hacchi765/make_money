# Suggested Commands for Development

## Setup
- `python -m venv venv`: Create virtual environment.
- `source venv/bin/activate`: Activate virtual environment.
- `pip install -r requirements.txt`: Install dependencies.

## Execution
- `python src/main.py --mode=test --count=1`: Run manually (test mode, 1 article).
- `python src/main.py --mode=run --count=3`: Run manually (prod mode, 3 articles).

## Hugo
- `cd blog && hugo server`: Start local dev server.
- `cd blog && hugo --minify`: Build static site.

## Deployment (Manual via Workflow)
- `docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/x-auto-poster-bot/app-repo/money-maker:latest .`: Build Docker image.
- `docker push us-central1-docker.pkg.dev/x-auto-poster-bot/app-repo/money-maker:latest`: Push image.
- `gcloud run jobs deploy money-maker-job ...`: Deploy job (consult `deploy_trend_blog.md` for full command).
- `gcloud run jobs execute money-maker-job --region us-central1`: Manually trigger the deployed job.
