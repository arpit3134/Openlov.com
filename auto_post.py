import requests
import os
import json
from datetime import datetime

# Direct Stable URL
api_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

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
        filename = f"articles/post-{date_str}.html"
        with open(filename, "w") as f:
            f.write(text)
        print(f"✅ BINGO! Article saved: {filename}")
    else:
        print("❌ Error Message:", data.get('error', {}).get('message', 'API check failed'))
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"❌ Python Error: {e}")
