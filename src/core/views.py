from flask import render_template, url_for, redirect, request
from flask_login import login_user, current_user, login_required, logout_user
from .app import app
from ..controler.user_controler import LoginForm, RegisterForm, create_admin, create_exposant
from ..controler.cle_controler import get_key
from ..controler.food_controleur import RepasForm
from .const import TYPE_ADMIN, TYPE_AUTEUR, TYPE_EXPOSANT, TYPE_INTERVENANT, TYPE_STAFF

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
        else:
            print("Unknown credentials...")

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
        key = get_key(form.key.data)
        if key != None:
            if key.typeUser == TYPE_ADMIN: # TO DO message c ok
                create_admin(form.name.data, form.last_name.data, form.birth_date.data, form.tel.data, form.mail.data,
                             form.password.data, form.remarque.data)
            elif key.typeUser == TYPE_EXPOSANT:
                create_exposant(form.name.data, form.last_name.data, form.birth_date.data, form.tel.data, form.mail.data,
                             form.password.data, form.remarque.data)
            else:
                redirect(url_for("food", name=form.name.data, last_name=form.last_name.data, birth_date=form.birth_date.data, tel=form.tel.data,
                                 mail=form.mail.data, password=form.password.data, remarque=form.remarque.data))
        else:
            print("Key not found...")
    elif len(form.errors) > 0:
        print(form.errors)

    return render_template("inscription.html", form=form)

@app.route("/food", methods=["GET", "POST"])
def food():
    # try:
    #     name = request.args.get("name", type=str)
    #     last_name = request.args.get("last", type=str)
    #     birth_date = request.args.get("birth", type=str)
    #     tel = request.args.get("tel", type=str)
    #     mail = request.args.get("mail", type=str)
    #     password = request.args.get("password", type=str)
    #     remarque = request.args.get("remarque", type=str)
    #     key_str = request.args.get("key", type=str)
    # except:
    #     return redirect(url_for('index'))
    
    # key = get_key(key_str)
    # if key is None or key.typeUser != TYPE_INTERVENANT or key.typeUser != TYPE_STAFF or key.typeUser != TYPE_AUTEUR:
    #     return redirect(url_for('index'))
    
    form = RepasForm()
    form.setup_choices()

    if form.validate_on_submit():
        pass

    return render_template("food.html", form=form)

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