from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER, TIME, SMALLINT
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

    def can_offer_launch(self, day:str, midi:bool) -> bool:
        for re in self.repas:
            if str(re.jour) == day and bool(re.estMidi) == midi and len(re.clients) < re.capacite:
                return True
        return False