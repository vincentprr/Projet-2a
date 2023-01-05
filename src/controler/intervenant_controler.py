from ..modeles.intervenant import Intervenant

def get_intervenant(**kwargs) -> list:
    if len(kwargs) == 0:
        return Intervenant.query.all()
    else:
        return Intervenant.query.filter_by(kwargs).all()