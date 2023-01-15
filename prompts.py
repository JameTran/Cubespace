import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_text(prompt : str) -> str:
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=64)
    return response.choices[0].text

