from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators

class Submissionform(FlaskForm):
	text = StringField('text',[validators.InputRequired(),validators.Length(min=2,max=10)])
	submit = SubmitField(label='View Intraday Chart')
	monthly = SubmitField(label='View Monthly Chart')
	download = SubmitField(label='Download Data')
