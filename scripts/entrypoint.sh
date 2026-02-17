#!/bin/bash
set -e

echo "Starting Automation Sequence..."

# 1. Fetch Trends & Generate Articles
echo ">>> Running AI Generator..."
python src/main.py --mode=run --count=3

# 2. Build Hugo Site
echo ">>> Building Hugo Site..."
cd blog
hugo --minify
cd ..

# 3. Deploy to Firebase Hosting
# Requires FIREBASE_TOKEN environment variable
if [ -z "$FIREBASE_TOKEN" ]; then
    echo "WARNING: FIREBASE_TOKEN is not set. Skipping deployment."
else
    echo ">>> Deploying to Firebase Hosting..."
    firebase deploy --only hosting --token "$FIREBASE_TOKEN" --project "$GOOGLE_CLOUD_PROJECT"
fi

echo "Automation Sequence Completed."
