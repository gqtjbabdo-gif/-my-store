import os
import requests
import json

def fetch_and_update():
    """
    Fetches match data from the football-data API and updates the local matches.json file.
    """
    # API endpoint for World Cup matches
    url = "https://api.football-data.org/v4/competitions/WC/matches"
    
    # Use the key directly (Note: It is safer to use environment variables)
    api_key = "6dfdbc970367471aac79265084134f31"
    headers = {'X-Auth-Token': api_key}
    
    try:
        # Request data from the API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
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
        
        # Save to file
        with open('matches.json', 'w', encoding='utf-8') as f:
            json.dump(formatted_matches, f, ensure_ascii=False, indent=4)
        
        print("Successfully updated matches.json")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_update()
