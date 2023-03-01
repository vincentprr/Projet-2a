from ..modeles.hotel import Hotel
from ..modeles.loger import Loger
from ..controler.user_controler import get_user_by_id
from ..core.database import db

def get_hotel_by_id(id:int) -> Hotel or None:
    return Hotel.query.get(id)

def create_hotel(name:str, addr:str, tel:str, mail:str, capacity:int) -> Hotel:
    hotel = Hotel(nomHotel=name, addresseHotel=addr, telHotel=tel, mailHotel=mail, capaciteHotel=capacity)
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