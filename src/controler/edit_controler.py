from ..modeles.maison_edition import MaisonEdition
from ..core.database import db

def create_maison_edition(name:str, num_stand:int) -> MaisonEdition:
    house = MaisonEdition(nomME=name, numStand=num_stand)
    db.session(house)
    db.session.commit()

    return house