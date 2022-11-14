from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT


class Auteur(db.Model):
    idP = db.Column("idP",db.Integer(unsigned=True),primary_key=True)