import ollama

# List of poem topics
topics = ["rain", "love", "freedom", "nature"]

for topic in topics:
    prompt = f"Write a short poem in English about {topic}."

    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n🎨 Topic: {topic}")
    print(f"📝 Poem:\n{response['message']['content']}")
