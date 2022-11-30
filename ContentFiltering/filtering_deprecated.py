import os
import requests
import json
import numpy as np

# API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Filtering endpoint
URL = "https://api.openai.com/v1/engines/content-filter-alpha-c4/completions"

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + OPENAI_API_KEY
}

# Data to be sent to the server
data = json.dumps({
    "prompt": "<|endoftext|>Ah shit, here we go again\n--\nLabel:",
    "max_tokens": 1,
    "temperature": 0.0,
    "top_p": 0
})

# print results
result = requests.post(URL, headers=headers, data=data)
print(json.dumps(result.json(), indent=2))
