import requests

def joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        json_data = response.json()
        arr = ({
            "setup": json_data['setup'],
            "punchline": json_data['punchline']
        },)
        return arr
    except (requests.RequestException, ValueError):
        
        arr = ({
            "setup": "Sorry, I couldn't fetch a joke at the moment.",
            "punchline": ""
        },)
        return arr
