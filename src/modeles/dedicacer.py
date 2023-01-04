from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Dedicacer(db.Model):
    __tablename__ = "DEDICACER"
    idP = db.Column("idP",INTEGER(unsigned=True),db.ForeignKey("AUTEUR.idP"),primary_key=True)
    idCre = db.Column("idCre",INTEGER(unsigned=True),db.ForeignKey("CRENEAU.idCre"),primary_key=True)