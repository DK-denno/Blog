from . import main
from .. import db
from flask import render_template,url_for,redirect
from ..models import User,Subscribers,Blogposts
from .forms import Subscribe,Blog
from ..email import mail_message

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
        return redirect(url_for('main.index'))
    return render_template('blogform.html',blog=blog)

@main.route('/post/<id>')
def full_blog(id):
    full_blog = Blogposts.query.filter_by(id=id)
    return render_template('fullblog.html',full_blog=full_blog)

