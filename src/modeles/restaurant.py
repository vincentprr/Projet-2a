from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER, TIME
from sqlalchemy.orm import backref

class Restaurant(db.Model):
    __tablename__ = "RESTAURANT"
    idRest = db.Column("idRest",INTEGER(unsigned=True),primary_key=True)
    nomRest = db.Column("nomRest",TEXT)
    ouvertureM = db.Column("ouvertureM",TIME)
    fermetureM = db.Column("fermetureM",TIME)
    ouvertureS = db.Column("ouvertureS",TIME)
    fermetureS = db.Column("fermetureS",TIME)
    repas = db.relationship("Repas",backref=backref("restaurant", uselist=False))