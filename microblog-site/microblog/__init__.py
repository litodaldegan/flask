from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

# initializes the app
app = Flask("microblog")
app.config.from_object('config')

# initializes the database instance
db = SQLAlchemy(app)

from microblog import models
# importing the blueprint instance
from webPage.views import webPage_blueprint

# registring the blueprint
app.register_blueprint(webPage.views.webPage_blueprint)
