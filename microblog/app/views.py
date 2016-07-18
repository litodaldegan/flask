from flask import render_template, flash, redirect, url_for
from flask import request, make_response, escape, session
from werkzeug import secure_filename
import datetime, os
from app import app
from app import db, models
from .forms import LoginForm
from .forms import SubmitPost

@app.route('/index')
@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/news')
def news():
	user = models.User.query.all()
	posts = models.Post.query.all()
	return render_template('news.html',
							title='New Posts',
							user=user,
							posts=posts)

@app.route('/newsmonth/<int:month>')
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

# Outro meio de fazer o roteamento
app.add_url_rule("/news2/",
					endpoint="news",
					view_func=news)

@app.route('/post', methods=['GET', 'POST'])
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

	# If the user is already log in
	elif 'username' in session:
		if form.post.data:
			users = models.User.query.all()

			nickname = session['username']
			
			for u in users:
				# Checking if the user is regitered
				print nickname
				print u
				if u.nickname == nickname:
					postMsg = models.Post(body=form.post.data, timestamp=datetime.datetime.utcnow(), author=u)
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

@app.route('/signin', methods=['GET', 'POST'])
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

    	# Registering user
		session['username'] = form.openid.data
    	user = models.User(nickname=form.openid.data, email=form.email.data)
    	db.session.add(user)
    	db.session.commit()
        flash('Hello %s. Welcome to FORUM.' %
              (form.openid.data))
        return redirect('/index')

    return render_template('signin.html', 
                           title='Sign In',
                           form=form)

@app.errorhandler(404)
def page_not_found(error):
	resp = make_response(render_template('page_not_found.html'), 404)
	resp.headers['X-Something'] = 'A value'
	return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))

# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)