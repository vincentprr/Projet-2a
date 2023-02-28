from ..modeles.hotel import Hotel
from ..core.database import db

def create_hotel(name:str, addr:str, tel:str, mail:str, capacity:int) -> Hotel:
    hotel = Hotel(nomHotel=name, addresseHotel=addr, telHotel=tel, mailHotel=mail, capaciteHotel=capacity)
    db.session.add(hotel)
    db.session.commit()

    return hotel