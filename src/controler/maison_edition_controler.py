from ..modeles.maison_edition import MaisonEdition

def get_maison_edition(**kwargs) -> list:
    if len(kwargs) == 0:
        return MaisonEdition.query.all()
    else:
        return MaisonEdition.query.filter_by(kwargs).all()