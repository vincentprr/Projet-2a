from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Creneau(db.Model):
    __tablename__ = "CRENEAU"
    idCre = db.Column("idCre",INTEGER(unsigned=True),primary_key=True)
    dateDebut = db.Column("dateDebut",db.DateTime)
    dateFin = db.Column("dateFin",db.DateTime)