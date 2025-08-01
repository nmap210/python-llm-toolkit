import ollama

# List of personality types
personalities = ["introvert", "extrovert", "creative", "analytical"]

for p in personalities:
    prompt = f"Suggest 2 career paths suitable for a {p} person."

    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n🧬 Personality: {p}")
    print(f"💼 Careers: {response['message']['content']}")
