import ollama

# Feelings list
feelings = ["happy", "sad", "angry", "stressed"]

# Loop through each emotion
for feeling in feelings:
    prompt = f"I'm feeling {feeling}. Give me one good piece of advice."

    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n🧠 Feeling: {feeling}")
    print(f"💬 Advice: {response['message']['content']}")
