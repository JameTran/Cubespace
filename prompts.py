import os
import openai
import requests


openai.api_key = os.getenv("OPENAI_API_KEY")


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
    image_url = generate_image("bananas in the style of Claude Monet")
    img_data = requests.get(image_url).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
    return response['data'][0]['url']

def main():
    image_url = generate_image("bananas in the style of Claude Monet")
    img_data = requests.get(image_url).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
if __name__ == "__main__":
    main()
