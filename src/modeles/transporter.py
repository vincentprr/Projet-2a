from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Mangeur(db.Model):
    idVoy = db.Column("idVoy",db.Integer(unsigned=True),primary_key=True)
    idP = db.Column("idP",db.Integer(unsigned=True),primary_key=True)