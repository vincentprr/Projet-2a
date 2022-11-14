from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Creneau(db.Model):
    idCreneau = db.Column("idCreneau",db.Integer,primary_key=True)
    dateDebut = db.Column("dateDebut",db.DateTime)
    dateFin = db.Column("dateFin",db.DateTime)