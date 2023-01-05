from ..modeles.cle import Cle

def use_cle(cle : str) -> bool:
    if cle_existe(cle):
        Cle.query.filter_by(cleAct = cle).delete()
        return True
    return False

def cle_existe(cle : str) -> bool:
    return Cle.query.filter_by(cleAct = cle).first() is not None