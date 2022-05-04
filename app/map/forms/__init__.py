from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()


class register_form(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
    ], description="Add location of city")
    long = StringField('Longitude', [
        validators.DataRequired(),
    ], description="longitude of city")
    lat = StringField('Latitude', [
        validators.DataRequired(),
    ], description="latitude of city")
    popul = IntegerField('Population', [
        validators.DataRequired(),
    ], description="population of the city")
    submit = SubmitField()


class location_edit_form(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
    ], description="Add location of city")
    long = StringField('Longitude', [
        validators.DataRequired(),
    ], description="longitude of city")
    lat = StringField('Latitude', [
        validators.DataRequired(),
    ], description="latitude of city")
    popul = IntegerField('Population', [
        validators.DataRequired(),
    ], description="population of the city")
    submit = SubmitField()
