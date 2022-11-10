from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Navette(db.Model):
    idNavette = db.Column("idNavette",db.Integer(unsigned=True),primary_key=True)
    capaciteNavette = db.Column("capaciteNavette",TINYINT(unsigned=True))