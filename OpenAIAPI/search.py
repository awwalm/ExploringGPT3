import os
import openai

# JSONL content documents
doc_json = '{"text": "plane"}\n{"text": "boat"}\n{"text": "spaceship"}\n{"text":"car"}'
with open("doc.jsonl", "w") as doc:
    doc.write(doc_json)
doc.close()

# Sending the query and documents to the API
openai.api_key = os.environ["OPENAI_API_KEY"]
response = openai.File.create(file=open("doc.jsonl"), purpose="search")
search_response = openai.Engine("babbage").search(
    search_model="babbage",
    query="A vehicle with wheels"
)

print(search_response)
