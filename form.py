from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class Contact(FlaskForm):
	names = StringField('Name : ', validators=[DataRequired()])
	email = StringField('Email : ', validators=[DataRequired(), Email()])
	subject = StringField('Subject : ', validators=[DataRequired()])
	message = TextAreaField('Message : ', validators=[DataRequired()])
	submit = SubmitField('Submit')

