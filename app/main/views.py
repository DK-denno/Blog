from . import main
from .. import db,photos
from flask import render_template,url_for,redirect,request
from ..models import User,Subscribers,Blogposts,Comments
from .forms import Subscribe,Blog,Comment,Delete
from ..email import mail_message
from flask_login import login_required

@main.route('/',methods=['GET','POST'])
def index():
    subscribe=Subscribe()
    if subscribe.validate_on_submit():
        subscriber = Subscribers(email=subscribe.email.data,username=subscribe.username.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Welcome","email/subscription",subscriber.email,subscriber=subscriber)
    bloggs=Blogposts.query.all()
    return render_template('index.html',subscribe=subscribe,bloggs=bloggs)

@main.route('/blog',methods=['GET','POST'])
def post():
  
    blog =Blog()
    if blog.validate_on_submit():
        blogs = Blogposts(title=blog.title.data,summary=blog.summary.data,post=blog.post.data)
        db.session.add(blogs)
        db.session.commit()
        
    return render_template('blogform.html',blog=blog)

@main.route('/post/<id>',methods=['GET','POST'])
def full_blog(id):
    full_blog = Blogposts.query.filter_by(id=id)
    commenting = Comment()
    delete = Delete()

    if commenting.validate_on_submit():
        comm = Comments(comment=commenting.comment.data,blog_id=id,username=commenting.username.data)
       
        db.session.add(comm)
        db.session.commit()
    commnents = Comments.query.filter_by(blog_id=id)
    return render_template('fullblog.html',delete=delete,comment=commenting,comm=commnents,full_blog=full_blog)
