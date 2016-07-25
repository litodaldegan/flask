from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

# initializes the app
app = Flask("app")
app.config.from_object('config')

# initializes the database instance
db = SQLAlchemy(app)

# importing the blueprint instance
from webPage.views import webPage_blueprint

# registring the blueprint
app.register_blueprint(webPage.views.webPage_blueprint)

