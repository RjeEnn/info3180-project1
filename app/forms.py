from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import StringField, PasswordField, SelectField
from wtforms.fields.core import DecimalField
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea

class UploadForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    noBedrooms = StringField('Number of Bedrooms', validators=[InputRequired()])
    noBathrooms = StringField('Number of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = DecimalField('Price', places=2, validators=[InputRequired()])
    propertyType = SelectField('Type', validators=[InputRequired()], choices=['House', 'Apartment'])
    description = StringField('Description', widget=TextArea())
    img = FileField('Photo (jpg/img)', validators=[FileRequired(), FileAllowed(['jpg', 'img'], 'Please Upload a valid image type (jpg/png)')])
