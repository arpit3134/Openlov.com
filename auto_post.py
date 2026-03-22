import requests
import os
import json
from datetime import datetime

api_key = os.getenv("GEMINI_API_KEY")
# List of models to try
models = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
success = False

for model in models:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    prompt = {"contents": [{"parts":[{"text": "Write a 300-word Hindi article about latest cricket. Use <h2> and <p> tags."}]}]}
    
    try:
        response = requests.post(url, json=prompt)
        data = response.json()
        if 'candidates' in data:
            article_text = data['candidates'][0]['content']['parts'][0]['text']
            date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
            os.makedirs("articles", exist_ok=True)
            filename = f"articles/post-{date_str}.html"
            with open(filename, "w") as f:
                f.write(article_text)
            print(f"✅ BINGO! Model '{model}' worked. Saved: {filename}")
            success = True
            break
    except:
        continue

if not success:
    print("❌ Saare models fail ho gaye. Ek baar API Key check karein.")
