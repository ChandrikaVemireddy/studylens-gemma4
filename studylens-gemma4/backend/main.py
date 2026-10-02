import json, os, re
from typing import Any
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types

load_dotenv()
MODEL = os.getenv('GEMMA_MODEL', 'gemma-4-31b-it')
API_KEY = os.getenv('GEMINI_API_KEY', '').strip()
app = FastAPI(title='StudyLens API', version='1.0.0')
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173','http://127.0.0.1:5173'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

def demo_result(question=None):
    return {'demo': True, 'model': 'demo-mode', 'explanation': 'Demo mode is active because GEMINI_API_KEY is not configured. Configure the key in backend/.env to run the real Gemma 4 model.', 'key_points': ['Upload an image containing study material.', 'Gemma 4 analyzes the image and explains the visible content.', 'The app can turn the same material into a short practice quiz.'], 'quiz': [{'question':'What makes StudyLens multimodal?','options':['It accepts images','It has CSS','It has a footer','It uses a button'],'answer':0,'explanation':'Images are an input modality alongside text.'},{'question':'Where should the API key stay?','options':['Backend environment','Public GitHub README','Frontend source','Screenshot'],'answer':0,'explanation':'Secrets should remain server-side and outside the repository.'}], 'follow_up': question or ''}

def call_gemma(image_bytes: bytes, mime_type: str, question: str | None) -> dict[str, Any]:
    client = genai.Client(api_key=API_KEY)
    prompt = '''You are the core study assistant in StudyLens.
Analyze the uploaded study image carefully. It may be a textbook page, diagram, handwritten note, or school-level question.

Return ONLY valid JSON with exactly these keys:
{
  "explanation": "A clear beginner-friendly explanation in 2-5 short paragraphs.",
  "key_points": ["3-6 concise key points"],
  "quiz": [{"question":"A useful practice question","options":["option A","option B","option C","option D"],"answer":0,"explanation":"Why the answer is correct"}],
  "follow_up": "A concise answer to the user's follow-up question, or an empty string."
}

Create 3 quiz questions based only on the uploaded image. If the image is unclear or contains no study content, say so and make the quiz empty.

Follow-up question:
''' + (question or '(none)')
    image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
    response = client.models.generate_content(model=MODEL, contents=[image_part, prompt], config=types.GenerateContentConfig(response_mime_type='application/json'))
    text = re.sub(r'^```json\s*|^```\s*|\s*```$', '', response.text.strip(), flags=re.I)
    result = json.loads(text)
    result['demo'] = False
    result['model'] = MODEL
    return result

@app.get('/api/health')
def health(): return {'ok': True, 'model': MODEL, 'configured': bool(API_KEY)}

@app.post('/api/analyze')
async def analyze(image: UploadFile = File(...), question: str | None = Form(default=None)):
    if not image.content_type or not image.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail='Please upload an image.')
    data = await image.read()
    if len(data) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail='Please use an image under 10 MB.')
    if not API_KEY: return demo_result(question)
    try: return call_gemma(data, image.content_type, question)
    except Exception as exc: raise HTTPException(status_code=502, detail=f'Gemma request failed: {exc}') from exc
