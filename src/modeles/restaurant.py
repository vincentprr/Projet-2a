from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER


class Restaurant(db.Model):
    __tablename__ = "RESTAURANT"
    idRest = db.Column("idRest",INTEGER(unsigned=True),primary_key=True)
    nomRest = db.Column("nomRest",TEXT)
    idCreM = db.Column("idCreM",INTEGER(unsigned=True))
    idCreS = db.Column("idCreS",INTEGER(unsigned=True))
    creneauM = db.relationship("Creneau",foreign_keys=[idCreM])
    creneauS = db.relationship("Creneau",foreign_keys=[idCreS])
    repas = db.relationship("Repas",backref="restaurant")