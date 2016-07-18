from flask import render_template, flash, redirect, url_for
from flask import request, make_response, Blueprint
from werkzeug import secure_filename
import datetime, os
from app.forms import LoginForm
from app.forms import SubmitPost
from app import models

noticias_blueprint = Blueprint ('noticias', __name__)

@noticias_blueprint.route('/')
def home():
	return render_template('home.html')

@noticias_blueprint.route('/noticias')
def about():
	return render_template('about.html')


@noticias_blueprint.route('/news')
def news():
	user = models.User.query.all()
	posts = models.Post.query.all()
	return render_template('news.html',
							title='New Posts',
							user=user,
							posts=posts)

@noticias_blueprint.route('/newsmonth/<int:month>')
def newsmonth(month):
	if month == None:
		return redirect('/news')

	user = models.User.query.all()
	posts = models.Post.query.all()
	posts2 = []

	for p in posts:
		if p.timestamp.month == month:	
			posts2.append(p)

	return render_template('news.html',
							title='New Posts',
							user=user,
							posts=posts2)

@noticias_blueprint.route('/post', methods=['GET', 'POST'])
def post():	
	form = SubmitPost()

	# if the fields is valid
	if form.validate_on_submit():
		users = models.User.query.all()

		for u in users:
			# Checking if the user is regitered
			nickname = u.nickname
			if form.openid.data == nickname:
				postMsg = models.Post(body=form.post.data, timestamp=datetime.datetime.utcnow(), author=u)
				db.session.add(postMsg)
				db.session.commit()
				return redirect('/news')

		flash('This user isn\'t registered')
		return redirect ('/signin')
	
	return render_template('post.html',
							title='Submite post',
							form=form)

@noticias_blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()

    # If the fields is valid
    if form.validate_on_submit():
    	users = models.User.query.all()
    	
    	for u in users:
    		# Checking if the user is already registered
    		x = u.nickname
    		if form.openid.data == x:
    			flash('This username is already in use. Chose another one.')
    			return redirect('/signin')

    		# Checking if the email is already registered
    		x = u.email
    		if form.openid.data == x:
    			flash('This email is already registered. Use another one.')
    			return redirect('/signin')

    	user = models.User(nickname=form.openid.data, email=form.email.data)
    	db.session.add(user)
    	db.session.commit()
        flash('Hello %s. Welcome to FORUM.' %
              (form.openid.data))
        return redirect('/index')

    return render_template('signin.html', 
                           title='Sign In',
                           form=form)

@noticias_blueprint.errorhandler(404)
def page_not_found(error):
	resp = make_response(render_template('page_not_found.html'), 404)
	resp.headers['X-Something'] = 'A value'
	return resp