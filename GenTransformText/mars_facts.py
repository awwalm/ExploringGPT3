import os
import requests
import json

# API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Completions endpoint
URL = "https://api.openai.com/v1/engines/davinci/completions"

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + OPENAI_API_KEY
}

# Data to be sent to the server
data = {
    'prompt': "I'm studying the planets. List things I should know about Mars.\n\n\
1. Mars is the nearest planet to Earth.\n\
2. Mars has seasons, dry variety (not as damp as Earth's).\n\
3. Mars' day is about the same length as Earth's (24.6 hours).\n\
4.",
    'temperature': 0,
    'max_tokens': 400,
    'top_p': 1,
    'frequency_penalty': 0.5,
    'presence_penalty': 0.5,
    'stop': ['11.']
}

# Result
result = requests.post(URL, headers=headers, data=json.dumps(data))
print(data["prompt"] + result.json()["choices"][0]["text"])
