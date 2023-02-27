from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import backref

class Mangeur(db.Model):
    __tablename__ = "MANGEUR"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("PERSONNE.idP"), primary_key=True)
    # regimes = db.relationship("Regime", secondary="AVOIR")
    # repas = db.relationship("Repas", secondary="MANGER")
    personne = db.relationship("Personne", backref=backref("mangeur", uselist=False), uselist=False)