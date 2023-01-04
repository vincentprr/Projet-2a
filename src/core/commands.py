from .app import app
from .database import db, create_tables

@app.cli.command()
def syncdb():
    """
    Create all table based on the models
    """
    create_tables(db)