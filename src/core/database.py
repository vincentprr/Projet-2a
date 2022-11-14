from flask_sqlalchemy import SQLAlchemy
from .app import app

try:
    db = SQLAlchemy(app)
except:
    print("Incorrect connection string for the database...")

def create_tables(database:SQLAlchemy) -> None:
    """
    Create all the models in the database.

    Parameters:
        database: a sql alchemy instance for a database
    """
    with app.app_context():
        database.create_all()