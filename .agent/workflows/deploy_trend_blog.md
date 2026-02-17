---
description: 自動収益化システム (Trend Blog Bot) のデプロイ手順
---

# 自動収益化システムのデプロイ

このワークフローは、作成したシステムをGoogle Cloudにデプロイし、完全自動化するための手順です。

## 前提条件
- GCPプロジェクト: `x-auto-poster-bot` (設定済み)
- Gemini API Key: `.env` に設定済み
- Firebase Hosting: 有効化済みであること

## 1. 必要な環境変数の確認
- `GEMINI_API_KEY`: `.env`を確認
- `FIREBASE_TOKEN`: Firebaseへのデプロイに必要。以下のコマンドで取得してください。
  ```bash
  firebase login:ci
  ```
  取得したトークンは `.env` に `FIREBASE_TOKEN=...` として追記してください。

## 2. Firebaseプロジェクトの初期化 (初回のみ)
// turbo
プロジェクトのルートでFirebase Hostingを初期化します。
```bash
firebase init hosting --project x-auto-poster-bot
# 設定:
# - public directory: blog/public
# - single-page app: No
# - automatic builds (GitHub): No
```

## 3. Dockerイメージのビルドとプッシュ
// turbo
Artifact Registryを使用します。（リポジトリ作成が必要な場合は作成）
```bash
gcloud artifacts repositories create app-repo --repository-format=docker --location=us-central1 --description="App Repository" || true
gcloud auth configure-docker us-central1-docker.pkg.dev
docker build -t us-central1-docker.pkg.dev/x-auto-poster-bot/app-repo/money-maker:latest .
docker push us-central1-docker.pkg.dev/x-auto-poster-bot/app-repo/money-maker:latest
```

## 4. Cloud Run Job のデプロイ
// turbo
環境変数を設定してJobを作成します。
```bash
gcloud run jobs deploy money-maker-job \
  --image us-central1-docker.pkg.dev/x-auto-poster-bot/app-repo/money-maker:latest \
  --location us-central1 \
  --set-env-vars GEMINI_API_KEY=$GEMINI_API_KEY \
  --set-env-vars FIREBASE_TOKEN=$FIREBASE_TOKEN \
  --set-env-vars GOOGLE_CLOUD_PROJECT=x-auto-poster-bot \
  --memory 2Gi \
  --max-retries 0
```

## 5. Cloud Scheduler の設定
// turbo
毎日3回（8時, 12時, 18時）自動実行するようにスケジューリングします。
```bash
gcloud scheduler jobs create http money-maker-schedule \
  --location us-central1 \
  --schedule="0 8,12,18 * * *" \
  --uri="https://us-central1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/x-auto-poster-bot/jobs/money-maker-job:run" \
  --http-method POST \
  --oauth-service-account-email $(gcloud auth list --filter=status:ACTIVE --format="value(account)")
```

## 完了
これでシステムは完全に自動化されました。Cloud Runのコンソールログで動作を確認できます。
