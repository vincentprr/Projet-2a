from ..core.database import db
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, SMALLINT

class Repas(db.Model):
    __tablename__ = "REPAS"
    idRepas = db.Column("idRepas",INTEGER(unsigned=True),primary_key=True)
    jour = db.Column("jour",db.Date)
    estMidi = db.Column("estMidi",TINYINT(unsigned=True))
    capacite = db.Column("capacite", SMALLINT(unsigned=True))
    idRest = db.Column("idRest",INTEGER(unsigned=True), db.ForeignKey("RESTAURANT.idRest"))