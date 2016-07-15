from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    email = StringField('openid', validators=[DataRequired()])

class SubmitPost(Form):
	openid = StringField('openid', validators=[DataRequired()])
	post = StringField('post', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)