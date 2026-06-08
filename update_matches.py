import requests
from bs4 import BeautifulSoup
import json

# URL of the Native Stats page
url = "https://native-stats.org/competition/fifa-world-cup/2026"

# Fetching the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

matches = []

# Scraping the match data
# Note: Ensure these selectors match the website's HTML structure
for row in soup.select('div.match-row'): 
    try:
        teams = row.select_one('.teams').text.strip()
        date = row.select_one('.date').text.strip()
        matches.append({
            "teams": teams,
            "date": date
        })
    except AttributeError:
        continue

# Saving the data to a JSON file
with open('matches.json', 'w', encoding='utf-8') as f:
    json.dump(matches, f, ensure_ascii=False, indent=4)

print("Data has been successfully fetched and saved!")
