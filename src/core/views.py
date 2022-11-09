from flask import render_template, url_for
from core.app import app

@app.route('/')
@app.route("/index.html")
@app.route("/index")
def index():
    return render_template("index.html")