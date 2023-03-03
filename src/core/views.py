from flask import render_template, url_for, redirect, request
from flask_login import login_user, current_user, login_required, logout_user
from .app import app
from .database import db
from ..controler.user_controler import LoginForm, RegisterForm, create_admin, create_exposant, create_staff, create_intervenant, create_author
from ..controler.cle_controler import get_key
from ..controler.food_controleur import RepasForm, create_eat, assign_regime
from ..controler.sleep_controler import SleepForm, create_loger
from ..controler.edit_controler import MaisonEditionForm, create_appartient
from .const import TYPE_ADMIN, TYPE_AUTEUR, TYPE_EXPOSANT, TYPE_INTERVENANT, TYPE_STAFF, JEUDI, VENDREDI, SAMEDI, DIMANCHE

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
                db.sesion.delete(key)
                db.session.commit()
            elif key.typeUser == TYPE_EXPOSANT:
                create_exposant(form.name.data, form.last_name.data, form.birth_date.data, form.tel.data, form.mail.data,
                             form.password.data, form.remarque.data)
                db.sesion.delete(key)
                db.session.commit()
            else:
                return redirect(url_for("food", name=form.name.data, last_name=form.last_name.data, birth_date=form.birth_date.data, tel=form.tel.data,
                                 mail=form.mail.data, password=form.password.data, remarque=form.remarque.data, key=form.key.data))
        else:
            print("Key not found...")
    elif len(form.errors) > 0:
        print(form.errors)

    return render_template("inscription.html", form=form)

@app.route("/food", methods=["GET", "POST"])
def food():
    try:
        name = request.args.get("name", type=str)
        last_name = request.args.get("last", type=str)
        birth_date = request.args.get("birth", type=str)
        tel = request.args.get("tel", type=str)
        mail = request.args.get("mail", type=str)
        password = request.args.get("password", type=str)
        remarque = request.args.get("remarque", type=str)
        key_str = request.args.get("key", type=str)
    except:
        return redirect(url_for('index'))
    
    key = get_key(key_str)
    if key is None or (key.typeUser != TYPE_INTERVENANT and key.typeUser != TYPE_STAFF and key.typeUser != TYPE_AUTEUR):
        return redirect(url_for('index'))
    
    form = RepasForm()
    form.setup_choices()

    if form.validate_on_submit():
        if key.typeUser == TYPE_STAFF:
            staff = create_staff(name, last_name, birth_date, tel, mail, password, remarque)
            
            if int(form.restaurantJeudiM.data) > 0:
                create_eat(staff.idP, form.restaurantJeudiM.data, JEUDI, True)
            if int(form.restaurantJeudiS.data) > 0:
                create_eat(staff.idP, form.restaurantJeudiS.data, JEUDI, False)

            if int(form.restaurantVendrediM.data) > 0:
                create_eat(staff.idP, form.restaurantVendrediM.data, VENDREDI, True)
            if int(form.restaurantVendrediS.data) > 0:
                create_eat(staff.idP, form.restaurantVendrediS.data, VENDREDI, False)

            if int(form.restaurantSamediM.data) > 0:
                create_eat(staff.idP, form.restaurantSamediM.data, SAMEDI, True)
            if int(form.restaurantSamediS.data) > 0:
                create_eat(staff.idP, form.restaurantSamediS.data, SAMEDI, False)

            if int(form.restaurantDimancheM.data) > 0:
                create_eat(staff.idP, form.restaurantDimancheM.data, DIMANCHE, True)
            if int(form.restaurantDimancheS.data) > 0:
                create_eat(staff.idP, form.restaurantDimancheS.data, DIMANCHE, False)

            for regime_id in form.regimes.data:
                assign_regime(regime_id, staff.idP)

            db.sesion.delete(key)
            db.session.commit()
        else:
            return redirect("sleep", name=name, last_name=last_name, birth_date=birth_date, tel=tel,
                            mail=mail, password=password, remarque=remarque, key=key_str, jM=form.restaurantJeudiM.data,
                            jS=form.restaurantJeudiS.data, vM=form.restaurantVendrediM.data, vS=form.restaurantVendrediS.data,
                            sM=form.restaurantSamediM.data, sS=form.restaurantSamediS.data, dM=form.restaurantDimancheM.data,
                            dS=form.restaurantDimancheS.data, regimes=','.join(form.regimes.data))

    return render_template("food.html", form=form)

@app.route("/sleep", methods=["GET", "POST"])
def sleep():
    try:
        name = request.args.get("name", type=str)
        last_name = request.args.get("last", type=str)
        birth_date = request.args.get("birth", type=str)
        tel = request.args.get("tel", type=str)
        mail = request.args.get("mail", type=str)
        password = request.args.get("password", type=str)
        remarque = request.args.get("remarque", type=str)
        key_str = request.args.get("key", type=str)
        jM = request.args.get("jS", type=str)
        jS = request.args.get("jS", type=str)
        vM = request.args.get("vM", type=str)
        vS = request.args.get("vS", type=str)
        sM = request.args.get("sM", type=str)
        sS = request.args.get("sS", type=str)
        dM = request.args.get("dM", type=str)
        dS = request.args.get("dS", type=str)
        regimes = request.args.get("regimes", type=str)
    except:
        return redirect(url_for('index'))
    
    key = get_key(key_str)
    if key is None or (key.typeUser != TYPE_INTERVENANT and key.typeUser != TYPE_AUTEUR):
        return redirect(url_for('index'))
    
    form = SleepForm()
    form.setup_choices()

    if form.validate_on_submit():
        if key.typeUser == TYPE_INTERVENANT:
            inter = create_intervenant(name, last_name, birth_date, tel, mail, password, remarque,
                                       form.arrivee.data, form.depart.data, form.use_car.data)
            if int(jM) > 0:
                create_eat(inter.idP, jM, JEUDI, True)
            if int(jS) > 0:
                create_eat(inter.idP, jS, JEUDI, False)

            if int(vM) > 0:
                create_eat(inter.idP, vM, VENDREDI, True)
            if int(vS) > 0:
                create_eat(inter.idP, vS, VENDREDI, False)

            if int(sM) > 0:
                create_eat(inter.idP, sM, SAMEDI, True)
            if int(sS) > 0:
                create_eat(inter.idP, sS, SAMEDI, False)

            if int(dM) > 0:
                create_eat(inter.idP, dM, DIMANCHE, True)
            if int(dS) > 0:
                create_eat(inter.idP, dS, DIMANCHE, False)

            for regime_id in regimes.split(','):
                assign_regime(int(regime_id), inter.idP)

            if int(form.hotelJeudi.data) > 0:
                create_loger(inter.idP, form.hotelJeudi.data, JEUDI)
            if int(form.hotelVendredi.data) > 0:
                create_loger(inter.idP, form.hotelVendredi.data, VENDREDI)
            if int(form.hotelSamedi.data) > 0:
                create_loger(inter.idP, form.hotelSamedi.data, SAMEDI)
            if int(form.hotelDimanche.data) > 0:
                create_loger(inter.idP, form.hotelDimanche.data, DIMANCHE)

            db.sesion.delete(key)
            db.session.commit()
        else:
            return redirect("travel", name=name, last_name=last_name, birth_date=birth_date, tel=tel,
                                mail=mail, password=password, remarque=remarque, key=key_str, jM=jM,
                                jS=jS, vM=vM, vS=vS, sM=sM, sS=sS, dM=dM, dS=dS, regimes=regimes,
                                hj=form.hotelJeudi.data, hv=form.hotelVendredi.data,
                                hs=form.hotelSamedi.data, hd=form.hotelDimanche.data,
                                arrivee=form.arrivee.data, depart=form.depart.data, car=form.use_car.data)
    
    return render_template("sleep.html", form=form)

@app.route("/author", methods=["GET", "POST"])
def travel():
    try:
        name = request.args.get("name", type=str)
        last_name = request.args.get("last", type=str)
        birth_date = request.args.get("birth", type=str)
        tel = request.args.get("tel", type=str)
        mail = request.args.get("mail", type=str)
        password = request.args.get("password", type=str)
        remarque = request.args.get("remarque", type=str)
        key_str = request.args.get("key", type=str)
        jM = request.args.get("jS", type=str)
        jS = request.args.get("jS", type=str)
        vM = request.args.get("vM", type=str)
        vS = request.args.get("vS", type=str)
        sM = request.args.get("sM", type=str)
        sS = request.args.get("sS", type=str)
        dM = request.args.get("dM", type=str)
        dS = request.args.get("dS", type=str)
        regimes = request.args.get("regimes", type=str)
        hJ = request.args.get("hJ", type=str)
        hV = request.args.get("hV", type=str)
        hS = request.args.get("hS", type=str)
        hD = request.args.get("hD", type=str)
        car = request.args.get("car", type=str)
        arrivee = request.args.get("arrivee", type=str)
        depart = request.args.get("depart", type=str)
    except:
        return redirect(url_for('index'))
    
    key = get_key(key_str)
    if key is None or key.typeUser != TYPE_AUTEUR:
        return redirect(url_for('index'))
    
    form = MaisonEditionForm()
    form.setup_choices()

    if form.validate_on_submit():
        inter = create_author(name, last_name, birth_date, tel, mail, password, remarque,
                                       arrivee, depart, car)
        if int(jM) > 0:
            create_eat(inter.idP, jM, JEUDI, True)
        if int(jS) > 0:
            create_eat(inter.idP, jS, JEUDI, False)

        if int(vM) > 0:
            create_eat(inter.idP, vM, VENDREDI, True)
        if int(vS) > 0:
            create_eat(inter.idP, vS, VENDREDI, False)

        if int(sM) > 0:
            create_eat(inter.idP, sM, SAMEDI, True)
        if int(sS) > 0:
            create_eat(inter.idP, sS, SAMEDI, False)

        if int(dM) > 0:
            create_eat(inter.idP, dM, DIMANCHE, True)
        if int(dS) > 0:
            create_eat(inter.idP, dS, DIMANCHE, False)

        for regime_id in regimes.split(','):
            assign_regime(int(regime_id), inter.idP)

        if int(hJ) > 0:
            create_loger(inter.idP, hJ, JEUDI)
        if int(hV) > 0:
            create_loger(inter.idP, hV, VENDREDI)
        if int(hS) > 0:
            create_loger(inter.idP, hS, SAMEDI)
        if int(hD) > 0:
            create_loger(inter.idP, hD, DIMANCHE)

        for m in form.maison.data:
            create_appartient(inter.idP, m)

        db.sesion.delete(key)
        db.session.commit()

    return render_template("author.html", form=form)

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