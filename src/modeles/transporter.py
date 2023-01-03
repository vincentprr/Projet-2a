from ..core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Transporter(db.Model):
    idVoy = db.Column("idVoy",INTEGER(unsigned=True),primary_key=True)
    idP = db.Column("idP",INTEGER(unsigned=True),primary_key=True)