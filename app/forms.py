  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Users
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators = [DataRequired()])
    password=PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    level= IntegerField('How many pushups can you do?', validators = [DataRequired()])
    submit=SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken')


class WorkoutForm(FlaskForm):
    exercise = StringField('Exercise')
    reps = IntegerField('Reps',
            validators = [DataRequired()]
            )
    
    submit = SubmitField('Finish workout')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
