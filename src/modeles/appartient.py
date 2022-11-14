from core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Appartient(db.Model):
    idP = db.Column("idP",INTEGER(unsigned=True),primary_key=True)
    idME = db.Column("idME",INTEGER(unsigned=True),primary_key=True)