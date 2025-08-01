import ollama

# List of English words
words = ["friend", "book", "flower", "teacher"]

for word in words:
    prompt = f"Translate the English word '{word}' into Bengali."

    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n📘 English: {word}")
    print(f"📗 Bengali: {response['message']['content']}")
