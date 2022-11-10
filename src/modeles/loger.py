from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Loger(db.Model):
    idLog = db.Column("idLog",db.Integer(unsigned=True),primary_key=True)
    idP = db.Column("idP",db.Integer(unsigned=True))
    idHotel = db.Column("idHotel",db.Integer(unsigned=True))
    jourLog = db.Column("jourLog",db.Date)
    