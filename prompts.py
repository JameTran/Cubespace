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
    '''with open('caption.txt', 'w') as f:
        f.write(response.choices[0].text)'''
    return response.choices[0].text

def generate_image(prompt : str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    img_data = requests.get(response['data'][0]['url']).content
    with open('./static/image_name.jpg', 'wb') as handler:
        handler.write(img_data)
    return response['data'][0]['url']

