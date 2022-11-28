"""
Based on Pradip Nichite's [GPT-3 GPT3Tutorial tutorial](
https://www.youtube.com/watch?v=ld3YbhoJz9w&ab_channel=PradipNichite). This should feature the updated semantic
search routine.

The embedding is an information dense representation of the semantic meaning of a piece of text. Each embedding is a
vector of floating point numbers, such that the distance between two embeddings in the vector space is correlated
with semantic similarity between two inputs in the original format. For example, if two texts are similar,
then their vector representations should also be similar.

**Use cases:**

- Text Similarity
- Semantic Search
- Classification
- Clustering
"""


import os
import numpy as np
import openai
import pandas as pd

# API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Text Similarity: captures semantic similarity between pieces of text.
document = ["eating food", "I am hungry", "I am traveling", "exploring new places"]
response = openai.Embedding.create(
    input=document,
    engine="text-similarity-curie-001"
)

# Interrogate response
print(*[f"{type(r)} | {len(r)}" for r in [response["data"], response["data"][0]]], sep='\n')
print(response["data"][0].keys())
print(response["data"][0]["embedding"])

# Embeddings (vector representation) for the contents of `document`
embedding_a = response['data'][0]['embedding']  # eating food
embedding_b = response['data'][1]['embedding']  # I am hungry
embedding_c = response['data'][2]['embedding']  # I am traveling
embedding_d = response['data'][3]['embedding']  # exploring new places

# Compare embeddings
print(np.dot(embedding_a, embedding_b))   # eating food vs I am hungry
print(np.dot(embedding_a, embedding_c))   # eating food vs I am traveling
print(np.dot(embedding_c, embedding_d))   # I am traveling vs exploring new places


# https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
# Precomputed embeddings
datafile_path = "https://cdn.openai.com/API/examples/data/fine_food_reviews_with_embeddings_1k.csv"
df = pd.read_csv(datafile_path)
df.head()
