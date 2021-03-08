from flask import render_template, redirect, url_for, request
from app.models import User, School, Student
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm
import os

API_KEY = os.environ.get("API_KEY")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		error = "validated"
		user = User.query.get(1)
		if user.check_password(form.password.data):
			login_user(user)
			return redirect(url_for('index'))
		else:
			error = 'Invalid password'
	return render_template('login.html', error=error, form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
	schools = School.query.all()
	return render_template('index.html', API_KEY=API_KEY, schools=schools)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))
