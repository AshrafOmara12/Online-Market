__author__ = 'Ashraf'
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'a90756c0a11d85beccbeb170'
db=SQLAlchemy(app)

from market import routes
