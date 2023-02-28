from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import backref

class Staff(db.Model):
    __tablename__ = "STAFF"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("MANGEUR.idP"), primary_key=True)
    mangeur = db.relationship("Mangeur", backref=backref("staff", uselist=False), uselist=False)
    creneaux = db.relationship("Creneau", secondary="TRAVAILLER")