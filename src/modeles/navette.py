from ..core.database import db
from sqlalchemy.dialects.mysql import TINYINT, INTEGER
from sqlalchemy.orm import backref

class Navette(db.Model):
    __tablename__ = "NAVETTE"
    idNavette = db.Column("idNavette",INTEGER(unsigned=True),primary_key=True)
    capaciteNavette = db.Column("capaciteNavette",TINYINT(unsigned=True))
    voyage = db.relationship("Voyage", backref=backref("navette", uselist=False), uselist=False)