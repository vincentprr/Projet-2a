from ..core.database import db
from sqlalchemy.dialects.mysql import TINYINT, INTEGER


class Voyage(db.Model):
    idVoy = db.Column("idVoy",INTEGER(unsigned=True),primary_key=True)
    heureDebVoy = db.Column("heureDebVoy",db.DateTime)
    dureeVoy = db.Column("dureeVoy",TINYINT)
    idNavette = db.Column("idNavette",INTEGER(unsigned=True))