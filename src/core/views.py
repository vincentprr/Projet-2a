from flask import render_template, url_for, request
from core.app import app

@app.route("/index.html")
@app.route("/index")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connexion', methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        pass

    return render_template("connexion.html")

@app.route('/inscription', methods=["GET", "POST"])
def inscription():
    if request.method == "POST":
        pass

    return render_template("inscription.html")