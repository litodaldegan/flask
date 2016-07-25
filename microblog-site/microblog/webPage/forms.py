from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

# form to be use in login page
class SigninForm(Form):
    userName = StringField('userName', [validators.Length(min=4, max=25)])
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', [validators.Length(min=4, max=24)])

# form to be use in the post page
class SubmitPost(Form):
	userName = StringField('userName', validators=[DataRequired()])
	post = StringField('post', validators=[DataRequired()])