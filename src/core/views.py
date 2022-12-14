from flask import render_template, url_for, redirect
from flask_login import login_user, current_user, login_required, logout_user
from .app import app
from ..controler.user_controler import LoginForm, RegisterForm

@app.route("/index.html")
@app.route("/index")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connexion', methods=["GET", "POST"])
def connexion():
    if current_user.is_authenticated:
        return redirect(url_for('feuille_de_route'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = form.get_auth_user()
        if user is not None:
            login_user(user)
            return redirect(url_for('feuille_de_route'))

    return render_template("connexion.html", form=form)

@app.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    return redirect(url_for('index'))

@app.route('/inscription', methods=["GET", "POST"])
def inscription():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        pass

    return render_template("inscription.html", form=form)

@app.route('/gestion')
@login_required
def gestion():
    return render_template("gestion.html")

@app.route('/feuille_de_route')
@login_required
def feuille_de_route():
    return render_template("feuilleRoute.html")

@app.route('/js/main')
def main_js():
    return render_template('js/main.js')

@app.route('/js/register')
def register_js():
    return render_template('js/register.js')