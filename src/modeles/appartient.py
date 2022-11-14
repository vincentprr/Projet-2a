from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Appartient(db.Model):
    idP = db.Column("idP",db.Integer(unsigned=True),primary_key=True)
    idME = db.Column("idME",db.Integer(unsigned=True),primary_key=True)