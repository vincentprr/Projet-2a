from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Travailler(db.Model):
    __tablename__ = "TRAVAILLER"
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("STAFF.idP"), primary_key=True)
    idCre = db.Column("idCre",INTEGER(unsigned=True),db.ForeignKey("CRENEAU.idCre"),primary_key=True)