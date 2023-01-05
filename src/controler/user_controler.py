from ..modeles.personne import Personne
from ..core.app import login_manager
from wtforms import StringField, PasswordField, EmailField
from flask_wtf import FlaskForm

@login_manager.user_loader
def get_user_by_id(id : int) -> Personne or None:
    return Personne.query.get(id)

def get_user(**kwargs) -> Personne or None:
    return Personne.query.filter_by(kwargs).first()

def get_users(**kwargs) -> list or None:
    if len(kwargs) == 0:
        return Personne.query.all()
    else:
        return Personne.query.filter_by(kwargs).all()

class LoginForm(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Password')

    def get_auth_user(self):
        user = get_user(email = self.email.data)
        return user if user is not None and user.password == self.password.data else None


class RegisterForm(FlaskForm):
    name = StringField("Name")