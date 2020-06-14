from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    regDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    level = db.Column(db.Integer, nullable=False) 
    
    def __repr__(self):
        return ''.join([
            'User: ',self.userid, " ",  self.login,  '\r\n',
            'D.O.B: ', self.dob, 'Date registered: ', self.regDate
            ])



class Workout(db.Model):
    workoutid = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=False)
    startDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    completionDate = db.Column(db.DateTime, nullable=False, default='Not Finished Yet')

    def __repr__(self):
        return ''.join([
            'WorkoutID: ',self.workoutid, " UserID:  ",  self.userid,  '\r\n',
            'Start date:  ', self.startDate, 'Completion Date: ', self.completionDate
            ])
