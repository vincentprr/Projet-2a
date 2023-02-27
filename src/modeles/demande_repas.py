from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER

class DemandeRepas(db.Model):
    __tablename__ = "DEMANDE_REPAS"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("MANGEUR.idP"), primary_key=True)
    mangeur = db.relationship("Mangeur", backref="demandes", uselist=False)
    jour = db.Column("jour",db.Date,primary_key=True)
    estMidi = db.Column("estMidi",TEXT)