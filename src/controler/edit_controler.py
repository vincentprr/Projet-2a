from flask_wtf import FlaskForm
from wtforms import SelectField
from ..core.utils import MultiCheckboxField
from ..modeles.maison_edition import MaisonEdition
from ..modeles.appartient import Appartient
from .user_controler import get_user_by_id
from ..core.database import db

def get_maison_edition_by_id(id:int) -> MaisonEdition or None:
    return MaisonEdition.query.get(id)

def get_maison_edition(**kwargs) -> MaisonEdition or None:
    return MaisonEdition.query.filter_by(**kwargs).all()

def create_maison_edition(name:str, num_stand:int) -> MaisonEdition:
    house = MaisonEdition(nomME=name, numStand=num_stand)
    db.session.add(house)
    db.session.commit()

    return house

def create_appartient(idA:int, idME:int) -> Appartient or None:
    app = None
    p = get_user_by_id(idA)

    if p != None and p.mangeur != None and p.mangeur.intervenant != None and p.mangeur.intervenant.auteur != None:
        maison = get_maison_edition_by_id(idME)
        if maison != None:
            app = Appartient(idP=idA, idME=idME)
            db.session.add(app)
            db.session.commit()

    return app

class MaisonEditionForm(FlaskForm):
    maison = MultiCheckboxField("Sélectionnez vos maison d'édition : ", choices=[])

    def setup_choices(self):
        for h in get_maison_edition():
            self.maison.choices.append((str(h.idME), h.nomME))