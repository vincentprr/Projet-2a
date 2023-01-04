from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Intervenant(db.Model):
    __tablename__ = "INTERVENANT"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("MANGEUR.idP"), primary_key=True)
    arrive = db.Column("arrive",db.DateTime)
    depart = db.Column("depart",db.DateTime)
    mangeur = db.relationship("Mangeur")
    loge = db.relationship("hotel", secondary="LOGER")
    voyage = db.relationship("voyage", secondary="TRANSPORTER")