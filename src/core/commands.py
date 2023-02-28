from .app import app
from .database import db, create_tables
from ..modeles.personne import Personne
from hashlib import sha256
from ..core.utils import crypt
from ..controler.food_controleur import create_restaurant, create_launch
from ..core.const import JEUDI, VENDREDI, SAMEDI, DIMANCHE

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

@app.cli.command()
def createsamplefoods():
    rest1 = create_restaurant("Le Poté", "12:00:00", "14:00:00", "18:00:00", "23:00:00")
    rest2 = create_restaurant("La Sauce du Chef", "12:00:00", "14:00:00", "18:00:00", "23:00:00")
    rest3 = create_restaurant("Burggy Funny", "12:00:00", "14:00:00", "18:00:00", "23:00:00")
    rest4 = create_restaurant("Chicken Douceur", "12:00:00", "14:00:00", "18:00:00", "23:00:00")

    create_launch(rest1.idRest, JEUDI, True, 1)
    create_launch(rest1.idRest, JEUDI, False, 1)
    create_launch(rest1.idRest, VENDREDI, True, 2)

    create_launch(rest2.idRest, VENDREDI, False, 500)
    create_launch(rest2.idRest, SAMEDI, False, 2)

    create_launch(rest3.idRest, SAMEDI, True, 5)

    create_launch(rest4.idRest, DIMANCHE, True, 12)
    create_launch(rest4.idRest, JEUDI, True, 12)