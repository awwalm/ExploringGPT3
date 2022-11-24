import os
import requests
import json

# Set up API key as environment variable
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Header
headers = {
    'Authorization': 'Bearer ' + OPENAI_API_KEY
}

# Send request and display results
result = requests.get("https://api.openai.com/v1/engines", headers=headers)
print(json.dumps(result.json(), indent=2))
