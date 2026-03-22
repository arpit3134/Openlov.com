import re
import os

# File path check karo (kyuki ab script folder ke andar hai)
file_path = "index.html"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    new_arts = """const ARTS=[
      {
        id:0,
        cat:'tech',
        tag:'tag-tech',
        lbl:'💻 Tech',
        em:'🚀',
        title:'Welcome to OpenLov — Your New AI Hub',
        desc:'Exploring the future of AI tools, dynamic web development, and the latest tech trends at OpenLov.com.',
        author:'Arpit',
        date:'Mar 22',
        read:'3 min',
        body:'Welcome to OpenLov.com! This platform is designed to be your go-to destination for discovering the most powerful AI tools and staying updated with tech innovations.\\\\n\\\\nOur mission is to simplify complex technology and provide useful resources for developers, creators, and tech enthusiasts. Stay tuned for more updates and deep dives into the world of AI!'
      }
    ];"""

    html = re.sub(r'const ARTS=\[.*?\];', new_arts, html, flags=re.DOTALL)
    new_trends = "const TRENDS=['Welcome to OpenLov.com','Latest AI Tools 2026','Developing Dynamic Websites'];"
    html = re.sub(r'const TRENDS=\[.*?\];', new_trends, html, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ Success: index.html cleaned and fake data removed!")
else:
    print("❌ Error: index.html not found in main directory")
