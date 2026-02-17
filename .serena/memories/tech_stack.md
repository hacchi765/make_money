# Tech Stack & Environment

- **Language**: Python 3.11, Bash
- **AI**: Google Gemini 1.5 Flash (via `google-generativeai` library)
- **SSG**: Hugo (Extended version)
- **Infrastructure**:
  - Google Cloud Run Jobs (Serverless Container)
  - Google Cloud Scheduler (Cron)
  - Firebase Hosting (CDN)
  - Google Artifact Registry (Docker Image)
- **Key Libraries**:
  - `google-generativeai`: Gemini API client
  - `feedparser`: RSS parsing
  - `requests`: HTTP requests
- **Environment Variables**:
  - `GEMINI_API_KEY`: API Key from Google AI Studio.
  - `FIREBASE_TOKEN`: CI token for Firebase deployment.
  - `GOOGLE_CLOUD_PROJECT`: GCP Project ID.
