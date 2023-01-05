from .app import app
from .database import db, create_tables
import click

@app.cli.command()
def syncdb():
    """
    Create all table based on the models
    """
    create_tables(db)

@app.cli.command()
@click.argument("username")
@click.argument("password")
@click.argument("user_type_id")
def createUser(username, password, user_type_id):
    """
    Create a new user
    """
    pass