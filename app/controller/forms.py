from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    street = StringField('Email', validators=[DataRequired()])
    city = StringField('Email', validators=[DataRequired()])
    state = StringField('Email', validators=[DataRequired()])     
    zipcode = StringField('Email', validators=[DataRequired()])     
    
    submit = SubmitField('Register')

    # def validate_email(self, email):
    #     user = UserDao.get_by_email(email.data)
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')

class HobbyForm(FlaskForm):
    name = StringField('Hobby Name', validators=[DataRequired()])

    submit = SubmitField('Save Hobby')