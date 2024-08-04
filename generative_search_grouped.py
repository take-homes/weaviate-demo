import weaviate

client = weaviate.connect_to_embedded(version="1.23.10")

try:
    questions = client.collections.get("Question")

    response = questions.generate.near_text(
        query="biology",
        limit=2,
        grouped_task="Write a tweet with emojis about these facts."
    )

    print(response.generated)  # Inspect the generated text

finally:
    client.close()  # Close client gracefully