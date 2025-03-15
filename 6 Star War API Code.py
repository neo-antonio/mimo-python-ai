import requests

def fetch_data(option):
    url = f"https://swapi.dev/api/{option}/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "results" in data:
            print(f"Number of entities: {len(data['results'])}")
            return data["results"]
        else:
            print("No results found.")
            return None

    except requests.HTTPError as e:
        print(f"Error: {e}")
        return None

while True:
    option = input("Enter what Star Wars data would you like to explore? (people, planets, starships): ").strip().lower()
    data = fetch_data(option)
    
    if data:
        for entity in data:
            print(entity["name"])
        
    else:
        print("Unable to download data.")
