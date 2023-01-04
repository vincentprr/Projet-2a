from ..core.database import db
from sqlalchemy.dialects.mysql import TEXT, INTEGER

class Cle(db.Model):
    __tablename__ = "CLE"
    id = db.Column("idC", INTEGER(unsigned=True), primary_key=True)
    cleAct = db.Column("cleActivation",TEXT)