from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    description = TextAreaField('Event Description', validators=[DataRequired()])
    date = StringField('Event Date (YYYY-MM-DD)', validators=[DataRequired()])
    venue = StringField('Event Venue', validators=[DataRequired()])
    type = StringField('Event Type', validators=[DataRequired()])
