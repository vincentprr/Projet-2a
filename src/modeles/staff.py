from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Staff(db.Model):
    __tablename__ = "STAFF"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("MANGEUR.idP"), primary_key=True)
    mangeur = db.relationship("Mangeur", backref="staff")
    creneaux = db.relationship("Creneau", secondary="TRAVAILLER")