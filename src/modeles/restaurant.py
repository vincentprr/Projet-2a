from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Restaurant(db.Model):
    idRest = db.Column("idRest",db.Integer(unsigned=True),primary_key=True)
    nomRest = db.Column("nomRest",TEXT)
    idCreneauM = db.Column("idCreneauM",db.Integer(unsigned=True))
    idCreneauS = db.Column("idCreneauS",db.Integer(unsigned=True))