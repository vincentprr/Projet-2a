from flask_wtf import FlaskForm
from wtforms import BooleanField
from ..modeles.restaurant import Restaurant
from ..core.database import db

def create_restaurant(name:str, openM:str, endM:str, openS:str, endS:str):
    db.session.add(Restaurant(nomRest=name, ouvertureM=openM, fermetureM=endM, ouvertureS=openS, fermetureS=endS))
    db.session.commit()

class RepasForm(FlaskForm):
    jeudiM = BooleanField()
    jeudiS = BooleanField()
    vendrediM = BooleanField()
    vendrediS = BooleanField()
    samediM = BooleanField()
    samediS = BooleanField()
    dimancheM = BooleanField()
    dimancheS = BooleanField()