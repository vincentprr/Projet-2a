from ..modeles.auteur import Auteur

def get_auteur(**kwargs) -> list:
    if len(kwargs) == 0:
        return Auteur.query.all()
    else:
        return Auteur.query.filter_by(kwargs).all()