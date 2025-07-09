# chatbot_app/websearch.py

import requests

SERPER_API_KEY = "58e900b939b36eba1a7f4ee9dcb40ce2cad84e0d"

def perform_web_search(query: str) -> str:
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "q": query
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        return "Failed to get search results."

    result = response.json()

    if not result.get("organic"):
        return "No search results found."

    # Format the top 3 results nicely
    output = "**Top Web Results:**\n\n"
    for item in result["organic"][:3]:
        output += f"[{item.get('title')}]({item.get('link')})\n"
        if item.get("snippet"):
            output += f"   {item['snippet']}\n\n"

    return output
