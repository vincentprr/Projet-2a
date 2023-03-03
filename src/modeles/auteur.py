from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import backref

class Auteur(db.Model):
    __tablename__ = "AUTEUR"
    idP = db.Column("idP", INTEGER(unsigned=True), db.ForeignKey("INTERVENANT.idP"), primary_key=True)
    # dedicaces = db.relationship("creneau", secondary="DEDICACER")
    maisons_editions = db.relationship("MaisonEdition", secondary="APPARTIENT", backref="auteurs")
    intervenant = db.relationship("Intervenant", backref=backref("auteur", uselist=False), uselist=False)