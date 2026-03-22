import requests
import os
import json
from datetime import datetime

api_key = os.getenv("GEMINI_API_KEY")
# Using Stable v1 API instead of beta
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"

prompt = {
    "contents": [{
        "parts":[{"text": "Write a unique 300-word Hindi article about latest cricket news. Use <h2> and <p> tags for HTML formatting."}]
    }]
}

headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, json=prompt, headers=headers)
    data = response.json()
    
    if 'candidates' in data:
        article_text = data['candidates'][0]['content']['parts'][0]['text']
        date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
        os.makedirs("articles", exist_ok=True)
        filename = f"articles/post-{date_str}.html"
        with open(filename, "w") as f:
            f.write(article_text)
        print(f"✅ BINGO! Article saved: {filename}")
    else:
        print("❌ Error from Gemini API:")
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"❌ Python Error: {e}")
