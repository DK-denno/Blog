from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,TextField,BooleanField,PasswordField
from wtforms.validators import Required,Email,EqualTo


class Signup(FlaskForm):
    Email = StringField('EMAIL-address',validators=[Required(),Email()])
    Username = StringField('USERNAME',validators=[Required()])
    Password = PasswordField('password',validators=[Required(), EqualTo('password2',message = 'Passwords must match')])    
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('SIGN IN')

    def validate_new_account(self,data_field):
        def validate_email(self,data_field):
            if User.query.filter_by(Email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(Username = data_field.data).first():
            raise ValidationError('That username is taken')


class Login(FlaskForm):
    Username = StringField('USERNAME',validators=[Required()])
    Password = PasswordField('password',validators=[Required()])
    submit = SubmitField('LOG IN')