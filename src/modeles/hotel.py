from ..core.database import db
from sqlalchemy.dialects.mysql import SMALLINT, TEXT, INTEGER
from sqlalchemy.orm import backref

class Hotel(db.Model):
    __tablename__ = "HOTEL"
    idHotel = db.Column("idHotel",INTEGER(unsigned=True),primary_key=True)
    nomHotel = db.Column("nomHotel",TEXT)
    adresseHotel = db.Column("adresseHotel",TEXT)
    telHotel = db.Column("telHotel",TEXT)
    mailHotel = db.Column("mailHotel",TEXT)
    capaciteHotel = db.Column("capaciteHotel",SMALLINT(unsigned=True))
    loges = db.relationship("Loger", backref=backref("hotel", uselist=False))