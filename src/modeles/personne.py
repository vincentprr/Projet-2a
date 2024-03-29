from ..core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT, INTEGER
from flask_login import UserMixin

class Personne(db.Model, UserMixin):
    __tablename__ = "PERSONNE"
    id = db.Column("idP", INTEGER(unsigned=True), primary_key=True)
    nom = db.Column("nomP", db.String(42))
    prenom = db.Column("prenomP", db.String(42))
    typeId = db.Column(TINYINT)
    date_naissance = db.Column("ddnP", db.Date)
    tel = db.Column("telP", db.String(11))
    email = db.Column("emailP", db.String(60))
    mdp = db.Column("mdpP", db.String(65))
    remarques = db.Column(TEXT)

    def get_id(self):
        return self.id