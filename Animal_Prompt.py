import ollama

# List of animals
animals = ["Elephant", "Penguin", "Tiger", "Dolphin"]

# Loop through each animal
for i, animal in enumerate(animals):
    # Create prompt using string + operator
    prompt = f"{i+1}. Tell me 2 interesting facts about a {animal}."

    # Get LLM response from local model
    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    # Print result
    print(f"\n🦄 Prompt: {prompt}")
    print(f"📢 Response: {response['message']['content']}")
