# importing the database instance
from microblog import db, lm
from flask.ext.login import LoginManager, UserMixin

# defining the table user
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(24))
    posts = db.relationship('Post', backref='author', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return 'nickname: ' + self.nickname

# defining the post table
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(225))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'title: ' + self.text + ', id: ' + str(self.id)

# defining the table for data to visualizations
class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(128), index=True)
    initial = db.Column(db.String(32), index=True)
    jobs = db.Column(db.Integer)
    totalEmployees = db.Column(db.Integer)
    totalSalary = db.Column(db.Integer)
    avgSalary = db.Column(db.Integer)
    year = db.Column(db.Integer)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))