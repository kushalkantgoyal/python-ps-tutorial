import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa8K\xd8]\x1cu;^&\t\xe0\xea/\xa6t\x7f\xfbs\x82\x99b\x97\xec\xdc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True

db = SQLAlchemy(app)
