from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class MaisonEdition(db.Model):
    idME = db.Column("idME",db.Integer(unsigned=True),primary_key=True)
    nomME = db.Column("nomME",TEXT)
    numStand = db.Column("numStand",db.SmallInteger(unsigned=True))