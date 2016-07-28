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
	dataJob = models.Job.query.all()

	jsData = []

	for data in dataJob:
		jsData.append({'state': data.state, 'initial': data.initial, 'jobs': data.jobs,
			'totalEmployees': data.totalEmployees,'totalSalary': data.totalSalary,
			'avgSalary': data.avgSalary, 'year': data.year })

	return jsonify(jsData) 