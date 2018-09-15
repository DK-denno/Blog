from . import db, login_manager
from flask_login import UserMixin, login_user
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index = True)
    user_name = db.Column(db.String(255),index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('YOU CANNOT ACCESS THIS DETAILS')

    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    @login_manager.user_loader
    def load_user(id):
       return User.query.get(int(id))

class Blogposts(UserMixin,db.Model):
    __tablename__= 'blogposts'
    id =db.Column(db.Integer,primary_key=True)
    title=db.column(db.String(1000))
    post=db.column(db.String(1000000))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comments',backref='comment',lazy="dynamic")

class Comments(UserMixin,db.Model):
    __tablename__ = 'comments'
    id =db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String(10000))
    blog_id=db.Column(db.Integer,db.ForeignKey('blogposts.id'))

class subscribers(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    comment = db.relationship('Comments',backref='comment',lazy="dynamic")
