import ollama

def get_llm_response(prompt, model='gemma:2b'):
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']

def print_llm_response(prompt, response):
    print("PROMPT:\n", prompt)
    print("\nRESPONSE:\n", response)
