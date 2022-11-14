from core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Loger(db.Model):
    idLog = db.Column("idLog",INTEGER(unsigned=True),primary_key=True)
    idP = db.Column("idP",INTEGER(unsigned=True))
    idHotel = db.Column("idHotel",INTEGER(unsigned=True))
    jourLog = db.Column("jourLog",db.Date)
    