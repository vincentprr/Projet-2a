from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Exposant(db.Model):
    idP = db.Column("idP",db.Integer(unsigned=True),primary_key=True)
    numStand = db.Column("numStand",db.SmallInteger(unsigned=True))