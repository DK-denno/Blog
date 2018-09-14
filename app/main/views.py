from . import main
from flask import render_template
from ..models import User

@main.route('/')
def index():
    return render_template('index.html')