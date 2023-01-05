from ..modeles.hotel import Hotel

def get_hotels(**kwargs) -> list:
    if len(kwargs) == 0:
        return Hotel.query.all()
    else:
        return Hotel.query.filter_by(kwargs).all()