from ..modeles.voyage import Voyage

def get_voyage(**kwargs) -> list:
    if len(kwargs) == 0:
        return Voyage.query.all()
    else:
        return Voyage.query.filter_by(kwargs).all()