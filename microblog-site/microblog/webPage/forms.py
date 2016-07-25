from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# form to be use in login page
class SigninForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired])

# form to be use in the post page
class SubmitPost(Form):
	openid = StringField('openid', validators=[DataRequired()])
	post = StringField('post', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)