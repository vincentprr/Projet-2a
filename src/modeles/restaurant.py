from core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER


class Restaurant(db.Model):
    idRest = db.Column("idRest",INTEGER(unsigned=True),primary_key=True)
    nomRest = db.Column("nomRest",TEXT)
    idCreneauM = db.Column("idCreneauM",INTEGER(unsigned=True))
    idCreneauS = db.Column("idCreneauS",INTEGER(unsigned=True))