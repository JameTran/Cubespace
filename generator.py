import os
import prompts
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
prompts.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        caption = prompts.Completion.create(
            model = "text-davinci-003",
            prompt = "",
            max_tokens = 64,
            temperature = 0.5      
        )
        image = prompts.Image.create(
            prompt = ""
        )

    return render_template("index.html")

