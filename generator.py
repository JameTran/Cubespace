import os
import prompts
import twitter
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

class DataStore():
    caption = None

data=DataStore()

@app.route("/", methods=["GET", "POST"])
def webapp2():
    return render_template("webapp2.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    caption_input = request.form.get('textname')
    image_input = request.form.get('imagename')

    prompt = prompts.generate_prompt(caption_input)
    caption = prompts.generate_text(prompt)
    data.caption = caption

    image_prompt = prompts.generate_image_prompt(image_input)
    image = prompts.generate_image(image_prompt)
    data.image = image

    if request.method == "POST":
        redirect("success.html")

    return render_template("upload.html", caption=caption, image=image)

@app.route("/success", methods=["GET", "POST"])
def success():
    twitter.create_tweet(data.caption, "./static/image_name.jpg")
    return render_template("success.html")

if __name__ == "__main__":
    app.run()