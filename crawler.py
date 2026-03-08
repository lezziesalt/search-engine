import requests
from bs4 import BeautifulSoup

urls = [
    "https://example.com",
    "https://wikipedia.org"
]

data = []

for url in urls:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.title.string if soup.title else "No title"
        text = soup.get_text()

        data.append({
            "url": url,
            "title": title,
            "content": text
        })

    except:
        pass

import json
with open("database.json","w") as f:
    json.dump(data,f)
