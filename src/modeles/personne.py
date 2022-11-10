from core.database import db
from sqlalchemy.dialects.mysql import TINYINT

class Personne(db.Model):
    id = db.Column("idP", db.Integer, primary_key=True)
    nom = db.Column("nomP", db.String(42))
    prenomP = db.Column(db.String(42))
    typeId = db.Column(TINYINT)
    ddnP = db.Column(db.Date)
    telP = db.Column(db.String(11))
    emailP = db.Column(db.String(60))
    mdpP = db.Column(db.String(65))