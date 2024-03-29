from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from .loger import Loger
from sqlalchemy.orm import backref

class Intervenant(db.Model):
    __tablename__ = "INTERVENANT"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("MANGEUR.idP"), primary_key=True)
    arrive = db.Column("arrive",db.DateTime)
    depart = db.Column("depart",db.DateTime)
    mangeur = db.relationship("Mangeur", backref=backref("intervenant", uselist=False), uselist=False)
    logements = db.relationship("Loger", backref="client")
    voyages = db.relationship("Voyage", secondary="TRANSPORTER", backref="voyageurs")
    use_car = db.Column("useCar", TINYINT(unsigned=True))

    def get_sleep(self, day:str) -> Loger or None:
        for loger in self.logements:
            if loger.jourLog == day:
                return loger
            
        return None