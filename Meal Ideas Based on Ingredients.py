import ollama

# Available ingredients
ingredients = ["potato", "rice", "egg", "spinach"]

for item in ingredients:
    prompt = f"Suggest a simple Indian meal recipe using {item}."

    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n🧂 Ingredient: {item}")
    print(f"🍛 Recipe: {response['message']['content']}")
