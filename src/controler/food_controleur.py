from flask_wtf import FlaskForm
from wtforms import BooleanField
from ..modeles.restaurant import Restaurant
from ..modeles.repas import Repas
from ..core.database import db

def get_restaurant_by_id(id_restaurant:int) -> Restaurant or None:
    return Restaurant.query.get(id_restaurant)

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
        res = True

    return repas

class RepasForm(FlaskForm):
    jeudiM = BooleanField()
    jeudiS = BooleanField()
    vendrediM = BooleanField()
    vendrediS = BooleanField()
    samediM = BooleanField()
    samediS = BooleanField()
    dimancheM = BooleanField()
    dimancheS = BooleanField()