import os
import openai
import requests


openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_text(prompt : str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
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


def generate_prompt(product):
    return """Write a creative ad for the following product to run on 
    Twitter using only 2 sentences:\n\nProduct: Learning Room is a virtual
     environment to help students from kindergarten to high school excel in 
     school.\n\nAd: Learn smarter and faster with Learning Room! Unlock your
      full potential and get ahead in school with our virtual learning 
      environment! #LearningRoom\n\nProduct: WordStream is an free app that 
      provides analysis on business reports.\n\nAd:\n \nGain valuable insights 
      into your business reports with WordStream! Make smarter decisions with 
      our free app. #WordStream\n\nProduct: HelloFresh is a meal kit company 
      that delivers fresh pre-made meal kits to your door.\n\nAd:\n\nSay 
      goodbye to meal planning stress with HelloFresh! Get fresh, pre-made 
      meals delivered to your door and enjoy delicious meals with ease. 
      #HelloFresh\n\nProduct: Curiosity Stream is a media streaming platform 
      that provides hundreds of hours of high quality education documentaries.
      \n\nAd:\n\nDive into the world of knowledge with Curiosity Stream! Get 
      access to hundreds of educational documentaries and explore your interests. 
      #CuriosityStream\n\nProduct:{} \n\nAd:""".format(product)

def generate_image_prompt(image):
    return "{} ,  in a minimalist, Flat, corporate style".format(image)

