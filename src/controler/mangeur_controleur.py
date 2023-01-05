from ..modeles.mangeur import Mangeur

def get_mangeur(**kwargs) -> list:
    if len(kwargs) == 0:
        return Mangeur.query.all()
    else:
        return Mangeur.query.filter_by(kwargs).all()