from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER

class Regime(db.Model):
    __tablename__ = "REGIME"
    idRegime = db.Column("idRegime",INTEGER(unsigned=True),primary_key=True)
    nomRegime = db.Column("nomRegime",TEXT)