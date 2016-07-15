from flask import render_template, flash, redirect
import datetime
from app import app
from app import db, models
from .forms import LoginForm
from .forms import SubmitPost

@app.route('/index')
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
		return redirect ('/login')

	return render_template('post.html',
							title='Submite post',
							form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # If the fields is valid
    if form.validate_on_submit():
    	users = models.User.query.all()
    	
    	for u in users:
    		# Checking if the user is already registered
    		x = u.nickname
    		if form.openid.data == x:
    			flash('This username is already in use. Chose another one.')
    			return redirect('/login')

    		# Checking if the email is already registered
    		x = u.email
    		if form.openid.data == x:
    			flash('This email is already registered. Use another one.')
    			return redirect('/login')

    	# Registering user
    	userName = models.User(nickname=form.openid.data, email=form.email.data)
    	db.session.add(userName)
    	db.session.commit()
        flash('Hello %s. Welcome to FORUM.' %
              (form.openid.data))
        return redirect('/index')

    return render_template('login.html', 
                           title='Sign In',
                           form=form)