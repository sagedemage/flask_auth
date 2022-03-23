from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

# print program
print("Hello")

class login_form(FlaskForm):
    """ Login Form """
    email = EmailField('Email Address', [
        validators.DataRequired(),
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    submit = SubmitField()


class register_form(FlaskForm):
    """ Registration Template """
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ],description="You need to signup with an email")

    # Enter password
    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.length(min=6, max=35)
    ],description="Create a password ")

    # Reenter password
    confirm = PasswordField('Repeat Password',description="Please retype your password to confirm it is correct")
    submit = SubmitField()