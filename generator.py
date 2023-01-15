import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        caption = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "",
            max_tokens = 64,
            temperature = 0.5      
        )
        image = openai.Image.create(
            prompt = ""
        )

    return render_template("index.html")

@app.route("/confirm", methods = ("GET", "POST"))
def confirm():
    return render_template("confirm.html")

@app.route("/success")
def success():
    return render_template("success.html")

