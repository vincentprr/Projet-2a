from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER


class Repas(db.Model):
    idRepas = db.Column("idRepas",INTEGER(unsigned=True),primary_key=True)
    jour = db.Column("jour",db.Date)
    estMidi = db.Column("estMidi",TEXT)
    idRest = db.Column("idRest",INTEGER(unsigned=True))