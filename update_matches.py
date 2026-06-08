import requests
from bs4 import BeautifulSoup
import json

def fetch_matches_data():
    """
    Fetches match information from the official competition statistics website 
    and saves it to a JSON file.
    """
    url = "https://native-stats.org/competition/fifa-world-cup/2026"
    
    # Using headers to mimic a real browser request, preventing 403 Forbidden errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors
        
        soup = BeautifulSoup(response.content, 'html.parser')
        all_matches = []
        
        # Searching for all table rows (tr)
        rows = soup.find_all('tr')
        
        for row in rows:
            columns = row.find_all('td')
            
            # Ensure the row contains data columns (at least 3: Date, Teams, Score)
            if len(columns) >= 3:
                match_data = {
                    "teams": columns[1].text.strip(),
                    "score": columns[2].text.strip(),
                    "date": columns[0].text.strip()
                }
                all_matches.append(match_data)
        
        # Saving the gathered data to a JSON file
        if all_matches:
            with open('matches.json', 'w', encoding='utf-8') as json_file:
                json.dump(all_matches, json_file, ensure_ascii=False, indent=4)
            print(f"Success: {len(all_matches)} matches were saved.")
        else:
            print("Warning: No match data found. Please verify the HTML structure.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: An issue occurred while fetching data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_matches_data()
    
