from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Admin(db.Model):
    __tablename__ = "ADMIN"
    idP = db.Column("idP", INTEGER(unsigned=True), db.ForeignKey("PERSONNE.idP"), primary_key=True)
    personne = db.relationship("Personne", backref="admin")