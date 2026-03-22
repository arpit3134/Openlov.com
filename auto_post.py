import requests
import os
import json
from datetime import datetime

api_key = os.getenv("GEMINI_API_KEY")

# 1. Sabse pehle available models ki list check karte hain
list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

try:
    models_data = requests.get(list_url).json()
    # Pura model path nikaalte hain (Jaise: models/gemini-1.5-flash)
    available_model = [m['name'] for m in models_data['models'] if 'generateContent' in m['supportedGenerationMethods']][0]
    print(f"✅ Found working model: {available_model}")

    # 2. Ab usi model se article likhwaate hain
    gen_url = f"https://generativelanguage.googleapis.com/v1beta/{available_model}:generateContent?key={api_key}"
    
    payload = {
        "contents": [{"parts": [{"text": "Write a 300-word Hindi article about Cricket trends in 2026. Use <h2> and <p> tags."}]}]
    }
    
    response = requests.post(gen_url, json=payload)
    article_text = response.json()['candidates'][0]['content']['parts'][0]['text']
    
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    os.makedirs("articles", exist_ok=True)
    filename = f"articles/post-{date_str}.html"
    
    with open(filename, "w") as f:
        f.write(article_text)
    
    print(f"🚀 BINGO! Article saved using {available_model}")

except Exception as e:
    print(f"❌ Ab bhi error hai bhai: {e}")
    if 'models_data' in locals(): print(json.dumps(models_data, indent=2))
