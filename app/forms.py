  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Users, Workout, Exercises, ExercisesInWorkout
from flask_login import login_user, current_user, logout_user

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

    set1 = IntegerField(" Enter your completed reps:",
            validators = [DataRequired()]
            )

    set2 = IntegerField(" Enter your completed reps:",
            validators = [DataRequired()]
            )

    set3 = IntegerField(" Enter your completed reps:",
            validators = [DataRequired()]
            )
    submit = SubmitField('Finish workout')


class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateRepsForm(FlaskForm):
    deleteWorkout= BooleanField('Delete latest workout')
    submit = SubmitField('Submit')
