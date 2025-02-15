import os
import openai

def call_llm(prompt: str):
    openai.api_key = os.getenv("AIPROXY_TOKEN")
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()