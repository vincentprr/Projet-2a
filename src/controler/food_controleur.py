from flask_wtf import FlaskForm
from wtforms import BooleanField
from ..modeles.restaurant import Restaurant
from ..modeles.repas import Repas
from ..modeles.manger import Manger
from ..core.database import db
from ..controler.user_controler import get_user_by_id

def get_restaurant_by_id(id_restaurant:int) -> Restaurant or None:
    return Restaurant.query.get(id_restaurant)

def get_repas_by_id(id_repas:int) -> Repas or None:
    return Repas.query.get(id_repas)

def create_restaurant(name:str, openM:str, endM:str, openS:str, endS:str) -> Restaurant:
    restaurant = Restaurant(nomRest=name, ouvertureM=openM, fermetureM=endM, ouvertureS=openS, fermetureS=endS)
    db.session.add(restaurant)
    db.session.commit()

    return restaurant

def create_launch(id_restaurant:int, day:str, midi:bool) -> Repas or None:
    repas = None
    restaurant = get_restaurant_by_id(id_restaurant)

    if restaurant != None:
        repas = Repas(jour=day, estMidi=midi, idRest=id_restaurant)
        db.session.add(repas)
        db.session.commit()

    return repas

def create_eat(id_mangeur:int, id_repas:int or None = None) -> Manger or None:
    manger = None
    mangeur = get_user_by_id(id_mangeur)

    if mangeur != None and mangeur.mangeur != None:
        repas = get_repas_by_id(id_repas)
        if repas != None:
            manger = Manger(idP=id_mangeur, idRepas=id_repas)
            db.session.add(manger)
            db.session.commit()

    return manger

class RepasForm(FlaskForm):
    jeudiM = BooleanField("Midi")
    jeudiS = BooleanField("Soir")
    vendrediM = BooleanField("Midi")
    vendrediS = BooleanField("Soir")
    samediM = BooleanField("Midi")
    samediS = BooleanField("Soir")
    dimancheM = BooleanField("Midi")
    dimancheS = BooleanField("Soir")