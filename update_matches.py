import os
import requests
import json

def fetch_and_update():
    """
    Fetches match data from the football-data API and updates the local matches.json file.
    """
    # API endpoint for World Cup matches
    url = "https://api.football-data.org/v4/competitions/WC/matches"
    
    # Retrieve API key from environment variables
    api_key = os.getenv('API_KEY')
    
    if not api_key:
        print("Error: API_KEY not found in environment variables.")
        return

    headers = {'X-Auth-Token': api_key}
    
    try:
        # Request data from the API
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Format the data
        formatted_matches = []
        for match in data.get('matches', []):
            formatted_matches.append({
                "homeTeam": {
                    "name": match['homeTeam']['name'], 
                    "code": match['homeTeam']['tla']
                },
                "awayTeam": {
                    "name": match['awayTeam']['name'], 
                    "code": match['awayTeam']['tla']
                },
                "score": {
                    "fullTime": {
                        "home": match['score']['fullTime']['home'], 
                        "away": match['score']['fullTime']['away']
                    }
                }
            })
        
        # Save the formatted data to matches.json
        with open('matches.json', 'w', encoding='utf-8') as f:
            json.dump(formatted_matches, f, ensure_ascii=False, indent=4)
        
        print("Successfully updated matches.json")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_update()
