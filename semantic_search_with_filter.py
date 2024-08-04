import weaviate
import weaviate.classes as wvc
import os
import requests
import json

client = weaviate.connect_to_embedded(version="1.23.10")

try:
    questions = client.collections.get("Question")

    response = questions.query.near_text(
        query="biology",
        limit=2,
        filters=wvc.query.Filter.by_property("category").equal("ANIMALS")
    )

    print(response.objects[0].properties)  # Inspect the first object

finally:
    client.close()  # Close client gracefully