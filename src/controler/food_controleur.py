from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField
from ..modeles.restaurant import Restaurant
from ..modeles.repas import Repas
from ..modeles.manger import Manger
from ..core.database import db
from ..controler.user_controler import get_user_by_id
from ..core.const import JEUDI, VENDREDI, SAMEDI, DIMANCHE

def get_restaurant_by_id(id_restaurant:int) -> Restaurant or None:
    return Restaurant.query.get(id_restaurant)

def get_restaurants(**kwargs) -> "list[Restaurant]":
    return Restaurant.query.filter_by(**kwargs).all()

def get_repas_by_id(id_repas:int) -> Repas or None:
    return Repas.query.get(id_repas)

def create_restaurant(name:str, openM:str, endM:str, openS:str, endS:str) -> Restaurant:
    restaurant = Restaurant(nomRest=name, ouvertureM=openM, fermetureM=endM, ouvertureS=openS, fermetureS=endS)
    db.session.add(restaurant)
    db.session.commit()

    return restaurant

def create_launch(id_restaurant:int, day:str, midi:bool, capacity:int) -> Repas or None:
    repas = None
    restaurant = get_restaurant_by_id(id_restaurant)

    if restaurant != None:
        repas = Repas(jour=day, estMidi=midi, idRest=id_restaurant, capacite=capacity)
        db.session.add(repas)
        db.session.commit()

    return repas

def create_eat(id_mangeur:int, id_repas:int) -> Manger or None:
    manger = None
    mangeur = get_user_by_id(id_mangeur)

    if mangeur != None and mangeur.mangeur != None:
        repas = get_repas_by_id(id_repas)
        if repas != None:
            manger = Manger(idP=id_mangeur, idRepas=id_repas)
            db.session.add(manger)
            db.session.commit()

    return manger

def get_availables_restaurants(day:str, midi:bool) -> "list[Restaurant]":
    res = []

    for restaurant in get_restaurants():
        if restaurant.can_offer_launch(day, midi):
            res.append(restaurant)

    return res

class RepasForm(FlaskForm):
    restaurantJeudiM = SelectField("Restaurant du Jeudi midi : ", choices=[(str(-1), "Je fais autrement.")])
    restaurantJeudiS = SelectField("Restaurant du Jeudi soir : ", choices=[(str(-1), "Je fais autrement.")])
    restaurantVendrediM = SelectField("Restaurant du Vendredi midi : ", choices=[(str(-1), "Je fais autrement.")])
    restaurantVendrediS = SelectField("Restaurant du Vendredi soir : ", choices=[(str(-1), "Je fais autrement.")])
    restaurantSamediM = SelectField("Restaurant du Samedi midi : ", choices=[(str(-1), "Je fais autrement.")])
    restaurantSamediS = SelectField("Restaurant du Samedi soir : ", choices=[(str(-1), "Je fais autrement.")])
    restaurantDimancheM = SelectField("Restaurant du Dimanche midi : ", choices=[(str(-1), "Je fais autrement.")])
    restaurantDimancheS = SelectField("Restaurant du Dimanche soir : ", choices=[(str(-1), "Je fais autrement.")])

    def setup_choices(self):
        for restau in get_availables_restaurants(JEUDI, True):
            self.restaurantJeudiM.choices.append((str(restau.idRest), restau.nomRest))

        for restau in get_availables_restaurants(JEUDI, False):
            self.restaurantJeudiS.choices.append((str(restau.idRest), restau.nomRest))

        for restau in get_availables_restaurants(VENDREDI, True):
            self.restaurantVendrediM.choices.append((str(restau.idRest), restau.nomRest))
        
        for restau in get_availables_restaurants(VENDREDI, False):
            self.restaurantVendrediS.choices.append((str(restau.idRest), restau.nomRest))

        for restau in get_availables_restaurants(SAMEDI, True):
            self.restaurantSamediM.choices.append((str(restau.idRest), restau.nomRest))

        for restau in get_availables_restaurants(SAMEDI, False):
            self.restaurantSamediS.choices.append((str(restau.idRest), restau.nomRest))

        for restau in get_availables_restaurants(DIMANCHE, True):
            self.restaurantDimancheM.choices.append((str(restau.idRest), restau.nomRest))

        for restau in get_availables_restaurants(DIMANCHE, False):
            self.restaurantDimancheS.choices.append((str(restau.idRest), restau.nomRest))
        