from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, SelectField, FloatField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed 

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    numBedrooms = IntegerField('Number of Bedrooms', validators=[InputRequired()])
    numBathrooms = FloatField('Number of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    propertyType = SelectField('Type', choices=['House', 'Apartment'], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', 
                    validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])