from core.database import db
from sqlalchemy.dialects.mysql import TINYINT

class Personne(db.Model):
    idP = db.Column(db.Integer, primary_key=True)
    nomP = db.Column(db.String(42))
    prenomP = db.Column(db.String(42))
    typeId = db.Column(TINYINT)