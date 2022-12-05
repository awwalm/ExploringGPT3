import os
import requests
import json
import numpy as np

# API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Filtering endpoint (https:// api.openai.com/v1/engines/content-filter-alpha-c4/completions)
# is subtly being phased out, Moderations is the updated means of content filtering
URL = "https://api.openai.com/v1/moderations"

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + OPENAI_API_KEY
}

# Data to be sent to the server
data = json.dumps({
    "model": "text-moderation-latest",
    "input": "Fuck that shit"
})

# print results
result = requests.post(URL, headers=headers, data=data)
print(json.dumps(result.json(), indent=2))
