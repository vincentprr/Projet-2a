from .core.app import app
from .core.database import db, create_tables
from .modeles import modeles
from .core.commands import *

app.run(debug=True)