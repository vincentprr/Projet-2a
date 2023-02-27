from ..modeles.personne import Personne
from ..modeles.admin import Admin
from ..modeles.exposant import Exposant
from ..core.app import login_manager
from ..core.database import db
from wtforms import StringField, PasswordField, EmailField, DateField
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from ..core.utils import crypt
from ..core.const import TYPE_STAFF, TYPE_INTERVENANT, TYPE_EXPOSANT, TYPE_AUTEUR, TYPE_ADMIN

@login_manager.user_loader
def get_user_by_id(id : int) -> Personne or None:
    return Personne.query.get(id)

def get_user(**kwargs) -> Personne or None:
    print(kwargs)
    return Personne.query.filter_by(**kwargs).first()

def get_users(**kwargs) -> list or None:
    if len(kwargs) == 0:
        return Personne.query.all()
    else:
        return Personne.query.filter_by(**kwargs).all()
    
def create_user(name:str, last_name:str, birth_date:str, tel:str, 
                mail:str, password:str, remarque:str, typeId:int) -> Personne:
    personne = Personne(nom=last_name, prenom=name, typeId=typeId, date_naissance=birth_date,
                            tel=tel, email=mail, mdp=crypt(password), remarques=remarque)
    db.session.add(personne)
    db.session.commit()

    return personne

def create_admin(name:str, last_name:str, birth_date:str, tel:str, 
                mail:str, password:str, remarque:str):
    p = create_user(name, last_name, birth_date, tel, 
                mail, password, remarque, TYPE_ADMIN)
    db.session.add(Admin(idP=p.id))
    db.session.commit()

def create_exposant(name:str, last_name:str, birth_date:str, tel:str, 
                mail:str, password:str, remarque:str):
    p = create_user(name, last_name, birth_date, tel, 
                mail, password, remarque, TYPE_EXPOSANT)
    db.session.add(Exposant(idP=p.id))
    db.session.commit()

class LoginForm(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Password')

    def get_auth_user(self):
        user = get_user(email=self.email.data)
        return user if user is not None and user.mdp == crypt(self.password.data) else None

class RegisterForm(FlaskForm):
    name = StringField("Prénom")
    last_name = StringField("Nom")
    birth_date = DateField("Date de naissance")
    tel = StringField("Téléphone")
    mail = EmailField("Email")
    password = PasswordField("Mot de passe")
    remarque = StringField("Remarques", widget=TextArea())
    key = StringField("Clé d'activation")