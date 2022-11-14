from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Hotel(db.Model):
    idHotel = db.Column("idHotel",db.Integer(unsigned=True),primary_key=True)
    nomHotel = db.Column("nomHotel",TEXT)
    adresseHotel = db.Column("adresseHotel",TEXT)
    telHotel = db.Column("telHotel",TEXT)
    mailHotel = db.Column("mailHotel",TEXT)
    capaciteHotel = db.Column("capaciteHotel",TINYINT(unsigned=True))