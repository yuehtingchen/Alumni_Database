from wtforms import Form, PasswordField, validators, SubmitField

class LoginForm(Form):
	password = PasswordField('New Password', validators=[validators.DataRequired()])
	submit = SubmitField('Sign In')