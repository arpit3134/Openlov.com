import re

# Hum poori file read karenge aur jahan ARTS array hai usse replace karenge
try:
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Naya clean data
    new_arts_data = """const ARTS=[
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
    body:'Welcome to OpenLov.com! This platform is designed to be your go-to destination for discovering the most powerful AI tools and staying updated with tech innovations.\\n\\nOur mission is to simplify complex technology and provide useful resources for developers, creators, and tech enthusiasts. Stay tuned for more updates and deep dives into the world of AI!'
  }
];"""
    
    new_trends_data = "const TRENDS=['Welcome to OpenLov.com','Latest AI Tools 2026','Developing Dynamic Websites'];"

    # Regex ko thoda aur open rakhte hain taaki har haal mein match ho
    content = re.sub(r'const ARTS\s*=\s*\[.*?\s*\]\s*;', new_arts_data, content, flags=re.DOTALL)
    content = re.sub(r'const TRENDS\s*=\s*\[.*?\s*\]\s*;', new_trends_data, content, flags=re.DOTALL)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Index.html is now CLEAN with 1 Post!")

except Exception as e:
    print(f"❌ Error: {e}")
