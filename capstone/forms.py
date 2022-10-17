from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email
class RegistrationForm(FlaskForm):
    username = StringField(lebel='username', validators=[DataRequired(), Length(min-3, max=20)])
    email = StringField(lebel='Email', validators=[DataRequired(),email()])
    password=PasswordField(lebel='Password', validators=[DataRequired(), Length(min=6, max=16)])
    comfirm_password=PasswordField(lebel='Confrim Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField(lebel='Signup')

class LoginForm(FlaskForm):
    email = StringField(lebel='Email', validators=[DataRequired(),Email()])
    password=PasswordField(lebel='Password', validators=[DataRequired(), Length(min=6, max=16)])

SubmitField=SubmitField(lebel='Login')