from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER, SMALLINT
from .auteur import Auteur

class MaisonEdition(db.Model):
    __tablename__ = "MAISON_EDITION"
    idME = db.Column("idME",INTEGER(unsigned=True),primary_key=True)
    nomME = db.Column("nomME",TEXT)
    numStand = db.Column("numStand",SMALLINT(unsigned=True))