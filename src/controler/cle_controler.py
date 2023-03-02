from ..modeles.cle import Cle
from ..core.database import db
from ..core.const import TYPE_ADMIN, TYPE_AUTEUR, ACTIVATION_KEY_LENGTH 
from random import choice
from string import ascii_letters, digits

def get_key(cle_activation:str) -> Cle:
    return Cle.query.filter_by(cleAct=cle_activation).first()

def create_key(typeUser:int, max_attemps:int = 100) -> Cle or None:
    cle = None

    if typeUser >= TYPE_ADMIN and typeUser <= TYPE_AUTEUR:
        attemp = 0
        while cle == None and attemp < max_attemps:
            key = ''.join([choice(ascii_letters + digits) for _ in range(ACTIVATION_KEY_LENGTH)])
            if get_key(key) == None:
                cle = Cle(cleAct=key, typeUser=typeUser)
                db.session.add(cle)
                db.session.commit()

    return cle