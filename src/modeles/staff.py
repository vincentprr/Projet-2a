from core.database import db
from sqlalchemy.dialects.mysql import INTEGER


class Staff(db.Model):
    idP = db.Column("idP",INTEGER(unsigned=True),primary_key=True)