from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Voyage(db.Model):
    idVoy = db.Column("idVoy",db.Integer,primary_key=True)
    heureDebVoy = db.Column("heureDebVoy",db.Datetime)
    dureeVoy = db.Column("dureeVoy",TINYINT)
    idNavette = db.Column("idNavette",db.Integer(unsigned=True))