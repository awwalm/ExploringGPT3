import os
import requests
import json

# Parameters
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
URL = "https://api.openai.com/v1/engines/davinci/completions"

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + OPENAI_API_KEY
}

# Data to be sent to the server
data = json.dumps({
    "prompt": "NICK FURY: There was an idea... to bring together a group of remarkable people...\nNICK FURY:...",
    "max_tokens": 50,
    "temperature": 0.1
})

result = requests.post(URL, headers=headers, data=data)
print(json.dumps(result.json(), indent=2))
