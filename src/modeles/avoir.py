from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Avoir(db.Model):
    idP = db.Column("idP", INTEGER(unsigned=True),primary_key=True)
    idRegime = db.Column("idRegime",db.Integer)