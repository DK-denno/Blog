from . import main
from flask import render_template
from ..models import User
from .forms import Subscribe

@main.route('/')
def index():
    subscribe=Subscribe()
    return render_template('index.html',subscribe=subscribe)