from core.database import db
from sqlalchemy.dialects.mysql import TINYINT, TEXT

class Cle(db.Model):
    cleAct = db.Column("cleActivation",TEXT,primary_key=True)