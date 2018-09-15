from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,TextField,BooleanField,PasswordField
from wtforms.validators import Required,Email,EqualTo

class Subscribe(FlaskForm):
    Email = StringField(render_kw={"placeholder":"you@gmail.com"},validators=[Required(),Email()])
    submit = SubmitField('SUBSCRIBE')

class Blog(FlaskForm):
    post = TextAreaField(render_kw={"placeholder":"you@gmail.com"},validators=[Required()])