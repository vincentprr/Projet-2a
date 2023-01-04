from ..modeles.personne import Personne
from ..core.app import login_manager

@login_manager.user_loader
def get_user_by_id(id : int) -> Personne:
    return Personne.query.get(id)

def get_users(**kwargs) -> list:
    if len(kwargs) == 0:
        return Personne.query.all()
    else:
        return Personne.query.filter_by(kwargs).all()

def login(login:str, password:str):
    """
    Function to connect a user
    """
    pass