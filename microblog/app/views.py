from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/index')
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route("/show_config")
def show_config():
	querystring_args = request.args.to_dict()
	post_args = request.form.to_dict()
	return jsonify(
		debug=current_app.config.get('DEBUG'),
		args=querystring_args,
		vars=post_args
    )

@app.route('/noticias')
def noticias():
	user = {'nickname': 'Miguel'}
	posts = [
		{ 
			'author': {'nickname': 'John'}, 
			'body': 'Beautiful day in Portland!' 
 		},
		{ 
			'author': {'nickname': 'Susan'}, 
			'body': 'The Avengers movie was so cool!' 
		}
	]
	return render_template('noticias.html',
							title='Noticias',
							user=user,
							posts=posts)

@app.route('/submeter')
def submeter():
	return render_template('submeter.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)