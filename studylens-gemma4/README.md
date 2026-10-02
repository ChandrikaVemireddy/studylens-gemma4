# StudyLens — Gemma 4 Multimodal Study Assistant

Hackathon prototype for **MLH Hacktoberfest Hack Day Hyderabad — Best Use of Gemma 4**.

Upload a study image and StudyLens uses **Gemma 4** to explain it, extract key points, generate a short quiz, and answer a follow-up question.

## Stack
React + Vite • Python + FastAPI • Google Gen AI Python SDK • Gemma 4

## Run

Backend:
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload --port 8000
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

Set `GEMINI_API_KEY` in `backend/.env`. The model defaults to `gemma-4-31b-it`.

Never commit `.env`.

The app has a clearly labeled demo mode when the key is absent, but the real hackathon demo should use the real Gemma 4 API.
