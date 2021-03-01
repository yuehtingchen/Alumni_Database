from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	password_hash = db.Column(db.String(120))

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	degree = db.Column(db.String(32))
	grad_year = db.Column(db.Integer)
	email = db.Column(db.String(64))
	linkedIn = db.Column(db.String(64))

	school_name = db.Column(db.String(128), db.ForeignKey('school.name'))

	def __repr__(self):
		return '<Student {}>'.format(self.name)

class School(db.Model):
	longitude = db.Column(db.Float, primary_key=True)
	latitude = db.Column(db.Float, primary_key=True)
	name = db.Column(db.String(128), index=True, unique=True)
	city = db.Column(db.String(32), index=True)
	country = db.Column(db.String(32), index=True)

	alumni = db.relationship('Student', backref = 'school', lazy = 'dynamic')

	def __repr__(self):
		return '<School {}>'.format(self.name)

@login.user_loader
def load_user(user_id):
	return User.query.get(user_id)

