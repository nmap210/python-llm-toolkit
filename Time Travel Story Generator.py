import ollama

# Years to travel
years = [1800, 1947, 2050, 3000]

for year in years:
    prompt = f"Imagine I time-traveled to the year {year}. Write a short story about what I might see there."

    response = ollama.chat(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n🕰️ Year: {year}")
    print(f"📚 Story: {response['message']['content']}")
