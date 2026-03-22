import os, requests
from datetime import datetime
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
def generate():
    prompt = "Write a 500-word SEO blog post in HTML about trending Tech or Finance. Use <h2> and <p> tags."
    res = requests.post(URL, json={"contents": [{"parts": [{"text": prompt}]}]})
    try:
        content = res.json()['candidates'][0]['content']['parts'][0]['text']
        os.makedirs("articles", exist_ok=True)
        filename = f"articles/post-{datetime.now().strftime('%Y%m%d')}.html"
        with open(filename, "w") as f:
            f.write(content)
        print("✅ Article Generated!")
    except: print("❌ Error")
generate()
