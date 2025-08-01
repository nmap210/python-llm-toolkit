import ollama

# List of relationships
relations = ["mother", "father", "friend", "girlfriend"]

for person in relations:
    prompt = f"Suggest a thoughtful birthday gift for my {person}."

    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n🎁 For: {person}")
    print(f"🎉 Suggestion: {response['message']['content']}")
