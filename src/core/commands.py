from .app import app
from .database import db, create_tables
from ..modeles.personne import Personne
from hashlib import sha256
from ..core.utils import crypt

@app.cli.command()
def syncdb():
    """
    Create all table based on the models
    """
    create_tables(db)

@app.cli.command()
def createsampleuser():
    """
    Create a new user
    """
    db.session.add(Personne(nom="Doe", prenom="John", typeId=1,
    date_naissance="1999-04-10", tel="0605020103", email="test@test.fr", mdp=crypt("test"), remarques="Nothing to say."))
    db.session.commit()
    print("User created")