import os
import openai

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"


def generate_text(prompt : str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=64
    )
    return response.choices[0].text

def generate_image(prompt : str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    #returns a URL
    return response['data'][0]['url']

def main():
    print(generate_text("Write a marketing blurb about bananas"))

    print(generate_image("bananas in the style of Claude Monet"))
if __name__ == "__main__":
    main()