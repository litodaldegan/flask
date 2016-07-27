#coding: utf-8

from flask import (
	jsonify, Blueprint
)
from microblog import models
from microblog.models import db

api_blueprint = Blueprint('api', __name__, static_folder='./static', template_folder='./templates')

@api_blueprint.route("/api-Users")
def api_Users():
	users = models.User.query.all()

	jsUsers = []

	for user in users:
		nickname = user.nickname
		email = user.email
		jsUsers.append({'nickname': nickname, 'email': email})

	return jsonify(jsUsers)

@api_blueprint.route("/api-Posts")
def api_Post():
	posts = models.Post.query.all()
	
	jsPosts = []

	for post in posts:
		body = post.body
		timestamp = post.timestamp
		nickname = models.User.query.get(post.user_id).nickname
		jsPosts.append({'body': body, 'timestamp': timestamp, 'nickname': nickname})

	return jsonify(jsPosts)

@api_blueprint.route("/api-Jobs")
def api_Jobs():
	data = [
	  {"State": "Alagoas", "Initial": "AL", "Jobs": 82, "connection": "direct", "Total Employees": 29762910, "Total Salary": 4792.84 ,"Average Salary": 31.38, "year": 2012},
	  {"State": "Amazonas",  "Initial": "AM", "Jobs": 140, "connection": "direct", "Total Employees": 34038822, "Total Salary": 2987.84 ,"Average Salary": 33.19, "year": 2012},
	  {"State": "Amapá", "Initial": "AP", "Jobs": 156, "connection": "direct", "Total Employees": 6627534, "Total Salary": 6840.55 ,"Average Salary": 39.77, "year": 2012},
	  {"State": "Bahia", "Initial": "BA", "Jobs": 852, "connection": "direct", "Total Employees": 131562282, "Total Salary": 5688.87 ,"Average Salary": 44.65, "year": 2012},
	  {"State": "Ceará", "Initial": "CE", "Jobs": 359, "connection": "direct", "Total Employees": 79938576, "Total Salary": 5440.54 ,"Average Salary": 43.04, "year": 2012},
	  {"State": "Goiás", "Initial": "GO", "Jobs": 209, "connection": "direct", "Total Employees": 80248428, "Total Salary": 5006.42 ,"Average Salary": 40.93, "year": 2012},
	  {"State": "Maranhão",  "Initial": "MA", "Jobs": 203, "connection": "direct", "Total Employees": 36731598, "Total Salary": 7047.82 ,"Average Salary": 30.27, "year": 2012},
	  {"State": "Pará",  "Initial": "PA", "Jobs": 453, "connection": "direct", "Total Employees": 58618824, "Total Salary": 6633.22 ,"Average Salary": 41.44, "year": 2012},
	  {"State": "Paraíba", "Initial": "PB", "Jobs": 67, "connection": "direct", "Total Employees": 36012192, "Total Salary": 5625.48 ,"Average Salary": 33.95, "year": 2012},
	  {"State": "Pernambuco",  "Initial": "PE", "Jobs": 1393, "connection": "direct", "Total Employees": 93733506, "Total Salary": 5203.44 ,"Average Salary": 38.35, "year": 2012},
	  {"State": "Piauí", "Initial": "PI", "Jobs": 235, "connection": "direct", "Total Employees": 23451540, "Total Salary": 4582.26 ,"Average Salary": 31.87, "year": 2012},
	  {"State": "Paraná",  "Initial": "PR", "Jobs": 2819, "connection": "direct", "Total Employees": 174765930, "Total Salary": 5606.76 ,"Average Salary": 41.83, "year": 2012},
	  {"State": "Rondônia",  "Initial": "RO", "Jobs": 429, "connection": "direct", "Total Employees": 19146756, "Total Salary": 6924.61 ,"Average Salary": 41.64, "year": 2012},
	  {"State": "Roraima", "Initial": "RR", "Jobs": 26, "connection": "direct", "Total Employees": 4021008, "Total Salary": 9147.32 ,"Average Salary": 36.8, "year": 2012},
	  {"State": "Tocantins", "Initial": "TO", "Jobs": 113, "connection": "direct", "Total Employees": 14462466, "Total Salary": 5938.05 ,"Average Salary": 36.5, "year": 2012},

	  {"State": "Alagoas", "Initial": "AL", "Jobs": 43, "connection": "direct", "Total Employees": 29762910, "Total Salary": 4792.84 ,"Average Salary": 31.38, "year": 2013},
	  {"State": "Amazonas",  "Initial": "AM", "Jobs": 235, "connection": "direct", "Total Employees": 34038822, "Total Salary": 2987.84 ,"Average Salary": 33.19, "year": 2013},
	  {"State": "Amapá", "Initial": "AP", "Jobs": 34, "connection": "direct", "Total Employees": 6627534, "Total Salary": 6840.55 ,"Average Salary": 39.77, "year": 2013},
	  {"State": "Bahia", "Initial": "BA", "Jobs": 567, "connection": "direct", "Total Employees": 131562282, "Total Salary": 5688.87 ,"Average Salary": 44.65, "year": 2013},
	  {"State": "Ceará", "Initial": "CE", "Jobs": 234, "connection": "direct", "Total Employees": 79938576, "Total Salary": 5440.54 ,"Average Salary": 43.04, "year": 2013},
	  {"State": "Goiás", "Initial": "GO", "Jobs": 590, "connection": "direct", "Total Employees": 80248428, "Total Salary": 5006.42 ,"Average Salary": 40.93, "year": 2013},
	  {"State": "Maranhão",  "Initial": "MA", "Jobs": 156, "connection": "direct", "Total Employees": 36731598, "Total Salary": 7047.82 ,"Average Salary": 30.27, "year": 2013},
	  {"State": "Pará",  "Initial": "PA", "Jobs": 321, "connection": "direct", "Total Employees": 58618824, "Total Salary": 6633.22 ,"Average Salary": 41.44, "year": 2013},
	  {"State": "Paraíba", "Initial": "PB", "Jobs": 334, "connection": "direct", "Total Employees": 36012192, "Total Salary": 5625.48 ,"Average Salary": 33.95, "year": 2013},
	  {"State": "Pernambuco",  "Initial": "PE", "Jobs": 900, "connection": "direct", "Total Employees": 93733506, "Total Salary": 5203.44 ,"Average Salary": 38.35, "year": 2013},
	  {"State": "Piauí", "Initial": "PI", "Jobs": 322, "connection": "direct", "Total Employees": 23451540, "Total Salary": 4582.26 ,"Average Salary": 31.87, "year": 2013},
	  {"State": "Paraná",  "Initial": "PR", "Jobs": 3242, "connection": "direct", "Total Employees": 174765930, "Total Salary": 5606.76 ,"Average Salary": 41.83, "year": 2013},
	  {"State": "Rondônia",  "Initial": "RO", "Jobs": 390, "connection": "direct", "Total Employees": 19146756, "Total Salary": 6924.61 ,"Average Salary": 41.64, "year": 2013},
	  {"State": "Roraima", "Initial": "RR", "Jobs": 12, "connection": "direct", "Total Employees": 4021008, "Total Salary": 9147.32 ,"Average Salary": 36.8, "year": 2013},
	  {"State": "Tocantins", "Initial": "TO", "Jobs": 123, "connection": "direct", "Total Employees": 14462466, "Total Salary": 5938.05 ,"Average Salary": 36.5, "year": 2013},

	  {"State": "Alagoas", "Initial": "AL", "Jobs": 54, "connection": "direct", "Total Employees": 29762910, "Total Salary": 4792.84 ,"Average Salary": 31.38, "year": 2014},
	  {"State": "Amazonas",  "Initial": "AM", "Jobs": 324, "connection": "direct", "Total Employees": 34038822, "Total Salary": 2987.84 ,"Average Salary": 33.19, "year": 2014},
	  {"State": "Amapá", "Initial": "AP", "Jobs": 43, "connection": "direct", "Total Employees": 6627534, "Total Salary": 6840.55 ,"Average Salary": 39.77, "year": 2014},
	  {"State": "Bahia", "Initial": "BA", "Jobs": 534, "connection": "direct", "Total Employees": 131562282, "Total Salary": 5688.87 ,"Average Salary": 44.65, "year": 2014},
	  {"State": "Ceará", "Initial": "CE", "Jobs": 344, "connection": "direct", "Total Employees": 79938576, "Total Salary": 5440.54 ,"Average Salary": 43.04, "year": 2014},
	  {"State": "Goiás", "Initial": "GO", "Jobs": 543, "connection": "direct", "Total Employees": 80248428, "Total Salary": 5006.42 ,"Average Salary": 40.93, "year": 2014},
	  {"State": "Maranhão",  "Initial": "MA", "Jobs": 231, "connection": "direct", "Total Employees": 36731598, "Total Salary": 7047.82 ,"Average Salary": 30.27, "year": 2014},
	  {"State": "Pará",  "Initial": "PA", "Jobs": 355, "connection": "direct", "Total Employees": 58618824, "Total Salary": 6633.22 ,"Average Salary": 41.44, "year": 2014},
	  {"State": "Paraíba", "Initial": "PB", "Jobs": 657, "connection": "direct", "Total Employees": 36012192, "Total Salary": 5625.48 ,"Average Salary": 33.95, "year": 2014},
	  {"State": "Pernambuco",  "Initial": "PE", "Jobs": 890, "connection": "direct", "Total Employees": 93733506, "Total Salary": 5203.44 ,"Average Salary": 38.35, "year": 2014},
	  {"State": "Piauí", "Initial": "PI", "Jobs": 342, "connection": "direct", "Total Employees": 23451540, "Total Salary": 4582.26 ,"Average Salary": 31.87, "year": 2014},
	  {"State": "Paraná",  "Initial": "PR", "Jobs": 2344, "connection": "direct", "Total Employees": 174765930, "Total Salary": 5606.76 ,"Average Salary": 41.83, "year": 2014},
	  {"State": "Rondônia",  "Initial": "RO", "Jobs": 546, "connection": "direct", "Total Employees": 19146756, "Total Salary": 6924.61 ,"Average Salary": 41.64, "year": 2014},
	  {"State": "Roraima", "Initial": "RR", "Jobs": 11, "connection": "direct", "Total Employees": 4021008, "Total Salary": 9147.32 ,"Average Salary": 36.8, "year": 2014},
	  {"State": "Tocantins", "Initial": "TO", "Jobs": 323, "connection": "direct", "Total Employees": 14462466, "Total Salary": 5938.05 ,"Average Salary": 36.5, "year": 2014}
	]; 
	return jsonify(data) 