# importing the database instance
from microblog import db

# defining the table user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username, email, posts):
        self.nickname = nickname
        self.email = email
        self.posts = posts

    def __repr__(self):
        return '<User %r>' % (self.nickname)

# defining the post table
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, body, timestamp, user_id):
        self.body = body
        self.timestamp = timestamp
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % (self.body)

# admin = User('admin', 'admin@example.com')

# db.create_all() # In case user table doesn't exists already. Else remove it.    

# db.session.add(admin)

# db.session.commit() # This is needed to write the changes to database

# User.query.all()

# User.query.filter_by(username='admin').first()