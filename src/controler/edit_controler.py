from flask_wtf import FlaskForm
from wtforms import SelectField
from ..modeles.maison_edition import MaisonEdition
from ..core.database import db

def get_maison_edition(**kwargs) -> MaisonEdition or None:
    return MaisonEdition.query.filter_by(**kwargs).all()

def create_maison_edition(name:str, num_stand:int) -> MaisonEdition:
    house = MaisonEdition(nomME=name, numStand=num_stand)
    db.session.add(house)
    db.session.commit()

    return house

class MaisonEditionForm(FlaskForm):
    maison = SelectField("Choisissez votre maison d'édition : ", choices=[])

    def setup_choices(self):
        for h in get_maison_edition():
            self.maison.choices.append((str(h.idME), h.nomME))