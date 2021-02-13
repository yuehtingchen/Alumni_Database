from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ChoiceType
from flask_migrate import Migrate
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	degree = db.Column(db.String(32))
	grad_year = db.Column(db.Integer)
	email = db.Column(db.String(64))
	linkedIn = db.Column(db.String(64))

	school_name = db.Column(db.String(128), db.ForeignKey('school.name'))

	def __repr__(self):
		return '<User {}>'.format(self.name)

class School(db.Model):
	longitude = db.Column(db.Float, primary_key=True)
	latitude = db.Column(db.Float, primary_key=True)
	name = db.Column(db.String(128), index=True, unique=True)
	city = db.Column(db.String(32), index=True)
	country = db.Column(db.String(32), index=True)

	alumni = db.relationship('User', backref = 'school', lazy = 'dynamic')

	def __repr__(self):
		return '<School {}>'.format(self.name)

