from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])     
    zipcode = StringField('Zipcode', validators=[DataRequired()])     
    
    submit = SubmitField('Save')

    # def validate_email(self, email):
    #     user = UserDao.get_by_email(email.data)
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')
