from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT


class Exposant(db.Model):
    idP = db.Column("idP", INTEGER(unsigned=True),primary_key=True)
    numStand = db.Column("numStand",SMALLINT(unsigned=True))