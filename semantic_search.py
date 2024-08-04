import weaviate

client = weaviate.connect_to_embedded(version="1.23.10")
try:
    questions = client.collections.get("Question")

    response = questions.query.near_text(
        query="biology",
        limit=2
    )

    print(response.objects[0].properties)

finally:
    client.close()  # Close client gracefully