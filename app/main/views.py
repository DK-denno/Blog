from . import main
from flask import render_template
from ..models import User
from .forms import Subscribe,Blog

@main.route('/',methods=['GET','POST'])
def index():
    subscribe=Subscribe()
    return render_template('index.html',subscribe=subscribe)

@main.route('/blog',methods=['GET','POST'])
def post():
    blog =Blog()
    return render_template('blogform.html',blog=blog)

