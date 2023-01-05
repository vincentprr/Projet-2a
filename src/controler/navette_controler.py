from ..modeles.navette import Navette

def get_navette(**kwargs) -> list:
    if len(kwargs) == 0:
        return Navette.query.all()
    else:
        return Navette.query.filter_by(kwargs).all()