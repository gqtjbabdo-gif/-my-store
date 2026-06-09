import os
import requests
import json

def fetch_and_update():
    """
    Fetches match data from the football-data API and updates the local matches.json file.
    """
    # API endpoint for World Cup matches
    url = "https://api.football-data.org/v4/competitions/WC/matches"
    
    # Securely retrieve API key from GitHub Secrets
    headers = {'X-Auth-Token': os.getenv('API_KEY')}
    
    try:
        # Request data from the API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        # Format the data to match the UI requirements (names and flag codes)
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
            
        # Write the formatted data to matches.json
        with open('matches.json', 'w', encoding='utf-8') as f:
            json.dump(formatted_matches, f, ensure_ascii=False, indent=4)
        
        print("Data updated successfully!")
        
    except requests.exceptions.RequestException as e:
        print(f"Network or API Error: {e}")
    except KeyError as e:
        print(f"Data format error (missing field): {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_and_update()
