from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Repas(db.Model):
    idRepas = db.Column("idRepas",db.Integer(unsigned=True),primary_key=True)
    jour = db.Column("jour",db.Date)
    estMidi = db.Column("estMidi",TEXT(unsigned=True))
    idRest = db.Column("idRest",db.Integer(unsigned=True))