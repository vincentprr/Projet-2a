from ..modeles.creneau import Creneau
from ..core.database import db

def get_or_create_creneau(start_date:str, end_date:str) -> Creneau:
    # TO DO
    db.session.add(Creneau(dateDebut=start_date, dateFin=end_date))
    db.session.commit()