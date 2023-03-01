from ..modeles.hotel import Hotel
from ..modeles.loger import Loger
from ..controler.user_controler import get_user_by_id
from ..core.database import db
from ..core.const import JEUDI, VENDREDI, SAMEDI, DIMANCHE
from flask_wtf import FlaskForm
from wtforms import SelectField

def get_hotel_by_id(id:int) -> Hotel or None:
    return Hotel.query.get(id)

def get_hotels(**kwargs) -> "list[Hotel]":
    return Hotel.query.filter_by(**kwargs).all()

def create_hotel(name:str, addr:str, tel:str, mail:str, capacity:int) -> Hotel:
    hotel = Hotel(nomHotel=name, adresseHotel=addr, telHotel=tel, mailHotel=mail, capaciteHotel=capacity)
    db.session.add(hotel)
    db.session.commit()

    return hotel

def create_loger(id_intervenant:int, id_hotel:int, jour:str) -> Loger or None:
    user = get_user_by_id(id_intervenant)

    if user != None and user.mangeur != None and user.mangeur.intervenant != None:
        hotel = get_hotel_by_id(id_hotel)
        if hotel != None:
            if user.mangeur.intervenant.get_sleep(jour) != None:
                loger = Loger(idP=user.id, idHotel=hotel.idHotel, jourLog=jour)
                db.session.add(loger)
                db.session.commit(loger)
                return loger

    return None

class SleepForm(FlaskForm):
    hotelJeudi = SelectField("Hotel du Jeudi : ", choices=[(str(-1), "Je fais autrement.")])
    hotelVendredi = SelectField("Hotel du Vendredi : ", choices=[(str(-1), "Je fais autrement.")])
    hotelSamedi = SelectField("Hotel du Samedi : ", choices=[(str(-1), "Je fais autrement.")])
    hotelDimanche = SelectField("Hotel du Dimanche : ", choices=[(str(-1), "Je fais autrement.")])

    def setup_choices(self):
        for hotel in get_hotels():
            if hotel.is_available(JEUDI):
                self.hotelJeudi.choices.append((str(hotel.idHotel), hotel.nomHotel))

        for hotel in get_hotels():
            if hotel.is_available(VENDREDI):
                self.hotelVendredi.choices.append((str(hotel.idHotel), hotel.nomHotel))

        for hotel in get_hotels():
            if hotel.is_available(SAMEDI):
                self.hotelSamedi.choices.append((str(hotel.idHotel), hotel.nomHotel))

        for hotel in get_hotels():
            if hotel.is_available(DIMANCHE):
                self.hotelDimanche.choices.append((str(hotel.idHotel), hotel.nomHotel))
