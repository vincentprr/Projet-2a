from flask import render_template, url_for, redirect
from flask_login import login_user
from .app import app
from ..controler.user_controler import LoginForm

@app.route("/index.html")
@app.route("/index")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connexion', methods=["GET", "POST"])
def connexion():
    form = LoginForm()

    if form.validate_on_submit():
        user = form.get_auth_user()
        if user is not None:
            login_user(user)
            return redirect(url_for('index'))

    return render_template("connexion.html", form=form)

@app.route('/inscription', methods=["GET", "POST"])
def inscription():
    return render_template("inscription.html")