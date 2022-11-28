import os
import requests
import json
import numpy as np

# API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Search endpoint (https://api.openai.com/v1/engines/<engine_id>/search) is deprecated,
# Embeddings is the updated means of conducting semantic search
URL = "https://api.openai.com/v1/embeddings"

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + OPENAI_API_KEY
}

# Data to be sent to the server
query = "A vehicle with wheels"
documents = ("plane", "boat", "spaceship", "car", query)
data = json.dumps({
    "model": "text-search-babbage-query-001",
    "input": documents
})

# Process response and store embeddings in dictionary
result = requests.post(URL, headers=headers, data=data)
embeddings = {documents[n]: result.json()["data"][n]["embedding"] for n in range(len(documents))}

# Evaluate embedding scores using dot products
dot_products = [
    np.dot(embeddings[query], embeddings[documents[n]]) for n in range(len(documents)-1)
]

print(f"{query} is most similar to {documents[dot_products.index(max(dot_products))]}")
