from ast import Sub
from wsgiref.validate import validator
from django.forms import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from gist.models import User
# import pycountry

class RegistrationForm(FlaskForm):

    firstname = StringField('First name', validators=[
                           DataRequired(), Length(min=2, max=20)])

    surname = StringField('Last name', validators=[
                           DataRequired(), Length(min=2, max=20)])                         

    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=7, max=20)])
    
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), Length(min=7, max=20), EqualTo('password')])
    
    submit = SubmitField('Sign Up')


    def validate_username(self, username):
    
        user = User.query.filter_by(username=username.data)
    
        if User:
             raise ValidationError('Our records show that this username is already registered on GIST.. Make sure yours is unique.')

    def validate_email(self, email):
    
        user = User.query.filter_by(email=email.data)
    
        if User:
             raise ValidationError('Our records show that this email is already registered on GIST.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=7, max=20)])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Log In')


# class CountrySelectField(SelectField):
#     def __init__(self, *args, **kwargs):
#         super(CountrySelectField, self).__init__(*args, **kwargs)
#         self.choices = [(country.alpha_2, country.name)
#                         for country in pycountry.countries]
