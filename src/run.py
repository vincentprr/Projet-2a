from core.app import app
from core.database import db, create_tables

if __name__ == "__main__":
    create_tables(db)
    app.run(debug=True)