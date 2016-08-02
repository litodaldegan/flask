from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin
import os

# function to get the environment variables
def get_env_variable(var_name, default=-1):
    try:
        return os.environ[var_name]
    except KeyError:
        if default != -1:
            return default
        error_msg = "Set the %s os.environment variable" % var_name
        raise Exception(error_msg)

# taking the variables
SECRET_KEY = get_env_variable("SECRET_KEY", True)
FACEBOOK_APP_SECRET = get_env_variable("FACEBOOK_APP_SECRET", True)
FACEBOOK_APP_ID = get_env_variable("FACEBOOK_APP_ID", True)

# initializes the app
app = Flask("microblog")
app.config.from_object('config')

# initializes the database instance
db = SQLAlchemy(app)
lm = LoginManager(app)

from microblog import models

# importing the blueprint instance
from webPage.views import webPage_blueprint
from api.views import api_blueprint
from visual.views import visual_blueprint

# registring the blueprint
app.register_blueprint(webPage.views.webPage_blueprint)
app.register_blueprint(api.views.api_blueprint)
app.register_blueprint(visual.views.visual_blueprint)


