import requests
import os
import json
from datetime import datetime

# API Key aur Direct URL
api_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

# Simple Prompt
payload = {
    "contents": [{
        "parts": [{"text": "Write a short 300-word SEO article in Hindi about Cricket. Use <h2> and <p> tags."}]
    }]
}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    if 'candidates' in data:
        text = data['candidates'][0]['content']['parts'][0]['text']
        date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
        os.makedirs("articles", exist_ok=True)
        with open(f"articles/post-{date_str}.html", "w") as f:
            f.write(text)
        print("✅ SUCCESS! Article created.")
    else:
        print("❌ Error Message:", data.get('error', {}).get('message', 'Unknown Error'))
except Exception as e:
    print(f"❌ Python Error: {e}")
