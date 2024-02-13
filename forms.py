from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class NewUserForm(FlaskForm):

    """A form for creating a new account using imported validators from wrforms"""
    
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):

    """Add an option where you can login with email OR account"""
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember User')

    submit = SubmitField('Login')

