from ..modeles.restaurant import Restaurant

def get_restaurant(**kwargs) -> list:
    if len(kwargs) == 0:
        return Restaurant.query.all()
    else:
        return Restaurant.query.filter_by(kwargs).all()