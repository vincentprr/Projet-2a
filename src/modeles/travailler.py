from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Travailler(db.Model):
    idCreneau = db.Column("idCreneau",db.Integer(unsigned=True),primary_key=True)
    idP = db.Column("idP",db.Integer(unsigned=True),primary_key=True)