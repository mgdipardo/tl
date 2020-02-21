from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    event_date = StringField('Event Date', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])
    submit = SubmitField('Submit')
