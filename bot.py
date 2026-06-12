import requests

weather = requests.get("https://wttr.in/?format=3").text

quote_data = requests.get(
    "https://zenquotes.io/api/random",
    timeout=10
).json()

quote = quote_data[0]["q"]
author = quote_data[0]["a"]

summary = f"""
=== DAILY PULSE ===

Weather:
{weather}

Quote:
"{quote}"
- {author}
"""

print(summary)

with open("daily_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)