from huggingface_hub import InferenceClient
import random
import time
import re



def format_prompt(message, custom_instructions=None):
    if custom_instructions:
        return f"[INST] {custom_instructions}\n\n{message} [/INST]"
    return f"[INST] {message} [/INST]"

def clean_response(response):
    # Remove any tags and unwanted content
    cleaned = re.sub(r'\[.*?\]', '', response) 
    cleaned = re.sub(r'https?://\S+', '', cleaned) 
    cleaned = re.sub(r'\d+ Answers', '', cleaned) 
    cleaned = re.sub(r'\n\s*\n', '\n', cleaned)
    return cleaned.strip()

def generate(prompt, temperature=0.7, max_new_tokens=256, top_p=0.95, top_k=50, repetition_penalty=1.2):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    
    top_p = float(top_p)
    
    generate_kwargs = {
        "temperature": temperature,
        "max_new_tokens": max_new_tokens,
        "top_p": top_p,
        "top_k": top_k,
        "repetition_penalty": repetition_penalty,
        "do_sample": True,
        "seed": random.randint(0, 10**7),
    }
    
    custom_instructions = """
    You are Algora, a helpful assistant. 
    1. Keep answers brief and focused (2-3 sentences).
2. Be clear and direct without extra elaboration.
    """
    
    formatted_prompt = format_prompt(prompt, custom_instructions)

    client = InferenceClient(API_URL, headers=headers)
    response = client.text_generation(formatted_prompt, **generate_kwargs)
    
    cleaned_response = clean_response(response)
    return cleaned_response

"""
print("Model has been started.............")

while True:
    user_prompt = input("User: ")
    
    start = time.time()
    
    generated_text = generate(user_prompt)
    end = time.time()
    print("Algora: ", generated_text)
    print(f"Time taken: {end - start:.2f}")
    
"""

if __name__ == "__main__":
    print("Model has been started.............")
    while True:
        user_prompt = input("User: ")
        start = time.time()
        generated_text = generate(user_prompt)
        end = time.time()
        print("Algora: ", generated_text)
        print(f"Time taken: {end - start:.2f}")