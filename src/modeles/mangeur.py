from core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Mangeur(db.Model):
    idP = db.Column("idP",INTEGER(unsigned=True),primary_key=True)