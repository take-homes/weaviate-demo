import weaviate

client = weaviate.connect_to_embedded(version="1.23.10")

try:
    questions = client.collections.get("Question")

    response = questions.generate.near_text(
        query="biology",
        limit=2,
        single_prompt="Explain {answer} as you might to a five-year-old."
    )

    print(response.objects[0].generated)  # Inspect the generated text

finally:
    client.close()  # Close client gracefully