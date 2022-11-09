from flask import Flask
from core.const import DATABASE_PROVIDER, DATABASE_HOST, DATABASE_PASS, DATABASE_USER, DATABASE_NAME, SESSION_KEY_LENGTH
from os import urandom

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# CONFIG #
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Release only
app.config['SQLALCHEMY_DATABASE_URI'] = "%s://%s:%s@%s/%s" % (DATABASE_PROVIDER, DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_NAME)
app.secret_key = urandom(SESSION_KEY_LENGTH)

import core.views