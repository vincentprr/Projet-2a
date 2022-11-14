from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Dedicacer(db.Model):
    idP = db.Column("idP",db.Integer(unsigned=True),primary_key=True)
    idCreneau = db.Column("idCreneau",db.Integer(unsigned=True),primary_key=True)