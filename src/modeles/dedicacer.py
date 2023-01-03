from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Dedicacer(db.Model):
    idP = db.Column("idP",INTEGER(unsigned=True),primary_key=True)
    idCreneau = db.Column("idCreneau",INTEGER(unsigned=True),primary_key=True)