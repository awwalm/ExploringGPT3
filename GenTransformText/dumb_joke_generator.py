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
    'prompt': 'Dumb Joke: I\'m not a vegetarian because I love animals. I\'m a vegetarian because I hate plants.\n###\n\
              Dumb Joke: Parallel lines have so much in common. \It\'s a shame they\'ll never meet.\n###\n\
              Dumb Joke: Someone stole my mood ring. I don\'t know how I feel about that.\n###\n\
              Dumb Joke:',
    'temperature': 0.5,
    'max_tokens': 100,
    'top_p': 1,
    'frequency_penalty': 0.5,
    'presence_penalty': 0.5,
    'stop': ['###']
}

# Result
result = requests.post(URL, headers=headers, data=json.dumps(data))
print(data["prompt"] + result.json()["choices"][0]["text"])
