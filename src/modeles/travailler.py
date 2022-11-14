from core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Travailler(db.Model):
    idCreneau = db.Column("idCreneau",INTEGER(unsigned=True),primary_key=True)
    idP = db.Column("idP",INTEGER(unsigned=True),primary_key=True)