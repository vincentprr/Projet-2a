from ..modeles.creneau import Creneau

def get_creneau(**kwargs) -> list:
    if len(kwargs) == 0:
        return Creneau.query.all()
    else:
        return Creneau.query.filter_by(kwargs).all()