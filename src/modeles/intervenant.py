from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Intervenant(db.Model):
    idP = db.Column("idP",db.Integer(unsigned=True),primary_key=True)
    arrive = db.Column("arrive",db.DateTime)
    depart = db.Column("depart",db.DateTime)