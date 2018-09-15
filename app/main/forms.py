from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,TextField,BooleanField,PasswordField
from wtforms.validators import Required,Email,EqualTo

class Subscribe(FlaskForm):
    email = StringField(render_kw={"placeholder":"you@gmail.com"},validators=[Required(),Email()])
    username = StringField(render_kw={"placeholder":"username"},validators=[Required()])

    submit = SubmitField('SUBSCRIBE')

class Blog(FlaskForm):
    title = StringField('TITLE',validators=[Required()])
    summary = StringField('SUMMARY',validators=[Required()])
    post = StringField('BLOG',validators=[Required()])
    submit = SubmitField('POST')
 
class Comment(FlaskForm):
    username = StringField(render_kw={"placeholder":"username"},validators=[Required()])
    comment = StringField(render_kw={"placeholder":"comment"},validators=[Required()])
    submit = SubmitField('POST')

class Delete(FlaskForm): 
    submit=SubmitField("DEL")