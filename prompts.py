import os
import openai
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")
<<<<<<< Updated upstream
=======
#openai.api_key = "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"
>>>>>>> Stashed changes


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
<<<<<<< Updated upstream
=======

def main():
    print(generate_text("Write a marketing blurb about bananas"))

    print(generate_image("bananas in the style of Claude Monet"))
    #img_data = requests.get(image_url).content
    #with open('image_name.jpg', 'wb')
if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
