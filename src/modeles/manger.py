from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Manger(db.Model):
    __tablename__ = "MANGER"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("MANGEUR.idP"), primary_key=True)
    idRepas = db.Column("idRepas",INTEGER(unsigned=True), db.ForeignKey("REPAS.idRepas"), primary_key=True)