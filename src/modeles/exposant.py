from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import backref

class Exposant(db.Model):
    __tablename__ = "EXPOSANT"
    idP = db.Column("idP", INTEGER(unsigned=True), db.ForeignKey("PERSONNE.idP"), primary_key=True)
    numStand = db.Column("numStand", SMALLINT(unsigned=True))
    personne = db.relationship("Personne", backref=backref("exposant", uselist=False), uselist=False)