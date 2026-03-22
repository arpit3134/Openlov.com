import requests
import os
import json
from datetime import datetime

api_key = os.getenv("GEMINI_API_KEY")
# Try using the most specific model path
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

prompt = {
    "contents": [{
        "parts":[{"text": "Write a 300-word Hindi article about Cricket news. Use HTML tags like <h2> and <p>."}]
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
