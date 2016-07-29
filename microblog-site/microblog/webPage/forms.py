from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

# form to be use in sign in page
class SigninForm(Form):
    userName = StringField('userName', [validators.Length(min=4, max=25)])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', [validators.Length(min=4, max=24)])


# form to be use in the post page
class SubmitPost(Form):
	post = StringField('post', [validators.Length(min=1, max=225)])


# form to be use in the login page
class LoginForm(Form):
	userName = StringField('userName', [validators.Length(min=4, max=25)])
	password = PasswordField('password', [validators.Length(min=4, max=24)])