from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Auteur(db.Model):
    __tablename__ = "AUTEUR"
    idP = db.Column("idP", INTEGER(unsigned=True), db.ForeignKey("INTERVENANT.idP"), primary_key=True)
    dedicaces = db.relationship("Creneau", secondary="DEDICACER")
    maisons_editions = db.relationship("MaisonEdition", secondary="APPARTIENT")
    intervenant = db.relationship("Intervenant", backref="auteur")