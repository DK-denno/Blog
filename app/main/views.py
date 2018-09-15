from . import main
from flask import render_template
from ..models import User
from .forms import Subscribe,Blog

@main.route('/')
def index():
    blog =Blog()
    subscribe=Subscribe()
    return render_template('index.html',blog=blog,subscribe=subscribe)

