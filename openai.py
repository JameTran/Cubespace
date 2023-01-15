import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Create promo copy for the FamilyTime mobile application. It allows unlimited uploading, special filters and makes it easy to create albums of photos and videos. It runs on iOS and Android:",
  temperature=0.5,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

def generate_text(prompt):
    prompt = "Create promo copy for the FamilyTime mobile application. It allows unlimited uploading, special filters and makes it easy to create albums of photos and videos. It runs on iOS and Android:"

print(response.choices[0].text)
