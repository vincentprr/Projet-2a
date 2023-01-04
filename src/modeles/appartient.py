from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Appartient(db.Model):
    __tablename__ = "APPARTIENT"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("AUTEUR.idP"), primary_key=True)
    idME = db.Column("idME",INTEGER(unsigned=True), db.ForeignKey("MAISON_EDITION.idME"), primary_key=True)