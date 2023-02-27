from ..modeles.cle import Cle

def get_key(cle_activation:str) -> Cle:
    return Cle.query.filter_by(cleAct=cle_activation).first()