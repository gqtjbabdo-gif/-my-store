import os
import requests
import json

def fetch_matches_data():
    # Official API endpoint for World Cup matches
    url = "https://api.football-data.org/v4/competitions/WC/matches"
    
    # Retrieve the API key from GitHub Secrets securely
    api_key = os.getenv('API_KEY') 
    headers = { 'X-Auth-Token': api_key }
    
    try:
        # Request data from the API
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        data = response.json()
        
        # Save the match data to matches.json
        with open('matches.json', 'w', encoding='utf-8') as f:
            json.dump(data.get('matches', []), f, ensure_ascii=False, indent=4)
        
        print("Success: Matches data updated successfully.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_matches_data()
    
