import os
import prompts
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
prompts.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        caption = prompts.generate_text(request.form("textname"))
        image = prompts.generate_text(request.form("imagename"))
        return redirect(url_for("index", caption=caption, image=image))

    caption = request.args.get("caption")
    image = request.args.get("image")
    return render_template("index.html", caption=caption, image=image)

