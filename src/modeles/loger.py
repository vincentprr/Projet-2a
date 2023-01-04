from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Loger(db.Model):
    __tablename__ = "LOGER"
    idLog = db.Column("idLog",INTEGER(unsigned=True),primary_key=True)
    idP = db.Column("idP",INTEGER(unsigned=True), db.ForeignKey("INTERVENANT.idP"))
    idHotel = db.Column("idHotel",INTEGER(unsigned=True), db.ForeignKey("HOTEL.idHotel"))
    jourLog = db.Column("jourLog",db.Date)
    