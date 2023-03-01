from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER

class Transporter(db.Model):
    __tablename__ = "TRANSPORTER"
    idVoy = db.Column("idVoy",INTEGER(unsigned=True),db.ForeignKey("VOYAGE.idVoy") ,primary_key=True)
    idP = db.Column("idP",INTEGER(unsigned=True),db.ForeignKey("INTERVENANT.idP") ,primary_key=True)