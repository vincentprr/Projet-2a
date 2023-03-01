from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Avoir(db.Model):
    __tablename__ = "AVOIR"
    idP = db.Column("idP", INTEGER(unsigned=True),db.ForeignKey("MANGEUR.idP"),primary_key=True)
    idRegime = db.Column("idRegime",INTEGER(unsigned=True), db.ForeignKey("REGIME.idRegime"), primary_key=True)