
from app import db, login_manager
from flask_login import UserMixin, current_user
from datetime import datetime

@login_manager.user_loader
def load_user(userid):
    return Users.query.get(int(userid))

class Users(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    regDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    level = db.Column(db.Integer, nullable=False) 
    
    workouts = db.relationship('Workout', backref='user', lazy =True)

    def get_id(self):
        return (self.userid)

    def __repr__(self):
        return ''.join([
            'User: ',self.userid, " ",  self.username,  '\r\n',
            'D.O.B: ', self.dob, 'Date registered: ', self.regDate
            ])



class Workout(db.Model):
    workoutid = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=False)
    startDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def create(self):
        new_workout = self(userid = current_user.userid)
        db.session.add(new_workout)
        db.session.commit()
    def __repr__(self):
        return ''.join([
            'WorkoutID: ',self.workoutid, " UserID:  ",  self.userid,  '\r\n'
            
            ])


class ExercisesInWorkout(db.Model):
    ex = db.Column(db.Integer, primary_key = True)
    
    
middle = db.Table('middle', 
    db.Column('workoutid',db.Integer, db.ForeignKey('workout.workoutid'), nullable=False),
    db.Column('exerciseid',db.Integer, db.ForeignKey('exercises.exerciseid'), nullable=False),
    db.Column('reps_completed',db.Integer, nullable=False, default =0)
)


class Exercises(db.Model):
    exerciseid = db.Column(db.Integer, primary_key = True)
    exercise = db.Column(db.String(30), nullable= False)
    threshold = db.Column(db.Integer, nullable=False, default = 20)
    workout = db.relationship("Workout", secondary=middle, backref =db.backref("work", lazy = 'dynamic'))
    def __repr__(self):
        return "".join([
            "ExerciseID: ", self.exerciseid, " Exercise: ", self.exercise, " Threshold: ", self.threshold])
