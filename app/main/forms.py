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
    post = TextAreaField('BLOG',validators=[Required()])
    submit = SubmitField('POST')
 
class Comment(FlaskForm):
    username = StringField(render_kw={"placeholder":"username"},validators=[Required()])
    comment = StringField(render_kw={"placeholder":"comment"},validators=[Required()])
    submit = SubmitField('POST')

class Delete(FlaskForm): 
    submit=SubmitField("DEL")

class Recovery(FlaskForm):
    email = StringField('Enter you last email',validators=[Required(),Email()])
    password = PasswordField('New password',validators=[Required(), EqualTo('password2',message = 'Passwords must match')])    
    password2 = PasswordField('Confirm Password',validators = [Required()])
    submit=SubmitField('Submit')