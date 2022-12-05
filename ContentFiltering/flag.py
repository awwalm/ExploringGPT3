import os
import requests
import json

# API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Filtering endpoint
URL = "https://api.openai.com/v1/engines/content-filter-alpha-c4/completions"

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + OPENAI_API_KEY
}

text_input = "What religion are you?"   # Text to be filtered
prompts = []    # Variable to hold an array of prompts
word_array = text_input.split()     # Splits text_input into words and stored in a list

# Prompts population
for word in word_array:
    prompts.append("<|endoftext|>" + word + "\n--\nLabel:")

# Data to be sent to server
data = json.dumps({
    "prompt": prompts,
    "max_tokens": 1,
    "temperature": 0.0,
    "top_p": 0
})

# print results
response = requests.post(URL, headers=headers, data=data)
for result in response.json()["choices"]:
    print(word_array[result["index"]] + " : " + result["text"])
