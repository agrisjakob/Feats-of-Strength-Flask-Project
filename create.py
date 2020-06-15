from app import db
from app.models import Users, Workout, ExercisesInWorkout, Exercises


db.drop_all()
db.create_all()

exercise1 = Exercises(exercise="Wall push-ups")
exercise2 = Exercises(exercise="Bent-knee push-ups")
exercise3 = Exercises(exercise="Push-ups")
exercise4 = Exercises(exercise="Archer push-ups")
exercise5 = Exercises(exercise="Sky diver push-ups")
exercise6 = Exercises(exercise="Negative one-handed push-ups", threshold= 10)
exercise7 = Exercises(exercise="One-handed pushups", threshold= 1)

db.session.add(exercise1)
db.session.add(exercise2)
db.session.add(exercise3)
db.session.add(exercise4)
db.session.add(exercise5)
db.session.add(exercise6)
db.session.add(exercise7)

db.session.commit()

