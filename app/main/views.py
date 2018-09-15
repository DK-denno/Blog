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
    if blog.validate_on_submit():
        post = 
   
