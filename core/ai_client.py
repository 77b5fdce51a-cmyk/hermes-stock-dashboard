import os
import requests

GEMINI_API_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
)

def ask_gemini(prompt: str, context: str = ""):
    if not GEMINI_API_KEY:
        raise RuntimeError("Missing GOOGLE_AI_STUDIO_API_KEY in .env")
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": context + "

" + prompt if context else prompt}
                ]
            }
        ]
    }
    resp = requests.post(GEMINI_URL, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return str(data)
