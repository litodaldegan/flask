from flask import (
	make_response, escape, session, Blueprint,
	render_template, flash, redirect, url_for, jsonify
)
import datetime, os
from microblog import models
from microblog.models import db
from .forms import SigninForm
from .forms import SubmitPost

webPage_blueprint = Blueprint('webPage', __name__, static_folder='./static', template_folder='./templates')

@webPage_blueprint.route('/index')
@webPage_blueprint.route('/home')
@webPage_blueprint.route('/')
def home():
	return render_template('home.html')

@webPage_blueprint.route('/about')
def about():
	return render_template('about.html')

@webPage_blueprint.route('/news')
def news():	
	posts = models.Post.query.all()
	return render_template('news.html',
							posts=posts)

@webPage_blueprint.route('/post', methods=['GET', 'POST'])
def post():	
	form = SubmitPost()

	# if the fields is valid
	if form.validate_on_submit():
		users = models.User.query.all()

		for u in users:
			# Checking if the user is regitered
			nickname = u.nickname
			if form.userName.data == nickname:
				postMsg = models.Post(user_id=u.id,
										body=form.post.data,
										timestamp=datetime.datetime.utcnow())
				db.session.add(postMsg)
				db.session.commit()
				return redirect('/news')

		flash('This user isn\'t registered')
		return redirect ('/signin')

	# If the user is already log in
	elif 'username' in session:
		if form.post.data:
			users = models.User.query.all()

			nickname = session['username']
			
			for u in users:
				# Checking if the user is regitered
				if u.nickname == nickname:
					postMsg = models.Post(user_id=u.id,
											body=form.post.data,
											timestamp=datetime.datetime.utcnow())
					db.session.add(postMsg)
					db.session.commit()
					# Logging user
					session['username'] = u.nickname
					return redirect('/news')

		else:
			return render_template('postByKnowUser.html',
									user=escape(session['username']),
									title='Submite post',
									form=form)
	
	return render_template('post.html',
							title='Submite post',
							form=form)

@webPage_blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    # If the fields is valid
    if form.validate_on_submit():
    	users = models.User.query.all()
    	
    	for u in users:
    		# Checking if the user is already registered
    		x = u.nickname
    		if form.userName.data == x:
    			flash('This username is already in use. Chose another one.')
    			return redirect('/signin')

    		# Checking if the email is already registered
    		x = u.email
    		if form.userName.data == x:
    			flash('This email is already registered. Use another one.')
    			return redirect('/signin')

    	# Registering user
		session['username'] = form.userName.data
    	user = models.User(nickname=form.userName.data, email=form.email.data)
    	db.session.add(user)
    	db.session.commit()
        flash('Hello %s. Welcome to FORUM.' %
              (form.userName.data))
        return redirect('/index')

    return render_template('signin.html', 
                           title='Sign In',
                           form=form)

@webPage_blueprint.route('/postTable')
def postTable():
	return render_template('postTable.html')

@webPage_blueprint.route("/api-Posts")
def api_Post():
	posts = models.Post.query.all()
	
	jsPosts = []

	for post in posts:
		body = post.body
		timestamp = post.timestamp
		nickname = models.User.query.get(post.user_id).nickname
		jsPosts.append({'body': body, 'timestamp': timestamp, 'nickname': nickname})

	return jsonify(jsPosts)

@webPage_blueprint.route('/userTable')
def userTable():
	return render_template('userTable.html')

@webPage_blueprint.route("/api-Users")
def api_Users():
	users = models.User.query.all()

	jsUsers = []

	for user in users:
		nickname = user.nickname
		email = user.email
		jsUsers.append({'nickname': nickname, 'email': email})

	return jsonify(jsUsers)

# @webPage_blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('webPage.home'))
#     return '''
#         <form action="" method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

@webPage_blueprint.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('webPage.home'))


@webPage_blueprint.route('/newsmonth/<int:month>')
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

# set the secret key.  keep this really secret:
webPage_blueprint.secret_key = os.urandom(24)