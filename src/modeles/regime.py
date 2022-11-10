from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Regime(db.Model):
    idRegime = db.Column("idRegime",db.Integer,primary_key=True)
    nomRegime = db.Column("nomRegime",TEXT)