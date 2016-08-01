from flask import (
    make_response, escape, session, Blueprint, request,
    render_template, flash, redirect, url_for, jsonify, Flask
)
import datetime, os
from flask_oauth import OAuth
from microblog import models
from microblog.models import db
from .forms import SigninForm, LoginForm, SubmitPost

webPage_blueprint = Blueprint('webPage', __name__,
                                static_folder='./static',
                                template_folder='./templates')

webPage_blueprint.secret_key = SECRET_KEY
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)


@webPage_blueprint.route('/loginFacebook')
def loginFacebook():
    return facebook.authorize(callback=url_for('webPage.facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@webPage_blueprint.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    user = facebook.get('/me')

    flash ('Logged in as id=%s name=%s redirect=%s email=%s genero=%s' % \
        (user.data['id'], user.data['name'], request.args.get('next'), user.data["email"], user.data["gender"]))

    session['username'] = user.data['name']
    user = models.User(nickname=user.data['name'],
                        email=user.data["email"],
                        password=user.data['id'])
    db.session.add(user)
    db.session.commit()

    return redirect('home')


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')



@webPage_blueprint.route('/index')
@webPage_blueprint.route('/home')
@webPage_blueprint.route('/')
def home():
    if 'username' in session:
        return render_template('home.html',
                                user=session['username'])

    return render_template('home.html')


@webPage_blueprint.route('/about')
def about():
    if 'username' in session:
        return render_template('about.html',
                                user=session['username'])

    return render_template('about.html')


@webPage_blueprint.route('/news')
def news():
    posts = models.Post.query.all()
    posts.reverse()

    if 'username' in session:
        return render_template('news.html',
                            posts=posts,
                            user=session['username'])
    
    return render_template('news.html',
                            posts=posts)


@webPage_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # If the fields is valid
    if form.validate_on_submit():
        users = models.User.query.all()

        for u in users:
            # Checking if the user is regitered
            nickname = u.nickname
            password = u.password
            if form.userName.data == nickname:
                if form.password.data == password:
                    session['username'] = form.userName.data
                    return render_template('home.html',
                            user=session['username'])

        flash("Incorrect login or password.")
        return render_template('login.html',
                            form=form)

    return render_template('login.html',
                            form=form)


@webPage_blueprint.route('/post', methods=['GET', 'POST'])
def post(): 
    form = SubmitPost()

    # If the user is log in
    if 'username' in session:
        if form.validate_on_submit():
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
                            return redirect('/news')

        return render_template('post.html',
                                user=escape(session['username']),
                                form=form)

    return redirect('/login')


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
        user = models.User(nickname=form.userName.data,
                            email=form.email.data,
                            password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Hello %s. Welcome to FORUM.' %
            (form.userName.data))
        return redirect('/index')

    return render_template('signin.html', 
                           form=form)


@webPage_blueprint.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('webPage.home'))


@webPage_blueprint.route('/postTable')
def postTable():
    return render_template('postTable.html')


@webPage_blueprint.route('/userTable')
def userTable():
    return render_template('userTable.html')


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