import unittest

from flask import url_for
from flask_testing import TestCase

from app import app, db, bcrypt
from app.models import Users, Workout, ExercisesInWorkout, Exercises
from os import getenv


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_URI'),
                SECRET_KEY=getenv('TEST_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True)
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()


        hashed_pw2 = bcrypt.generate_password_hash('test')
        employee = Users(username="test", password= hashed_pw2, level=3)
        db.session.add(employee)
        employeeWorkout = Workout(userid=1)
        db.session.add(employeeWorkout)
        
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


        
        ex1 = ExercisesInWorkout(exerciseid =1, workoutid=1)
        ex2 = ExercisesInWorkout(exerciseid =2, workoutid=1)
        ex3 = ExercisesInWorkout(exerciseid=3, workoutid=1)

        db.session.add(ex1)
        db.session.add(ex2)
        db.session.add(ex3)
        db.session.commit()
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_about_view(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code,200)

    def test_register_view(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code,200)

    def test_login_view(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code,200)

    def test_workout_view(self):
        with self.client:
            self.client.post('/login',
                    data=dict(
                    username ="test",
                    password ="test"))
            response = self.client.get('/workout')
            self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        with self.client:
            self.client.post('/login',
                    data=dict(
                    username ="test",
                    password ="test"), follow_redirects = True)
            response = self.client.get(url_for('logout'))
            self.assertRedirects(response, '/login')
            
    def test_log_view(self):
        with self.client:    
            self.client.post('/login',
                    data=dict(
                        username ="test",
                        password ="test"), follow_redirects=True)
            response= self.client.get('/log')
            self.assertEqual(response.status_code, 200)


class TestFunctionality(TestBase):

    def test_login(self):

        with self.client:
            response= self.client.post('/login',
                    data=dict(
                        username ="test",
                        password ="test"))
            self.assertRedirects(response, '/workout')
    
    def test_logging_workout(self):


        with self.client:
            self.client.post('/login',
                    data=dict(
                        username ="test",
                        password ="test"), follow_redirects=True)
            response = self.client.post('/workout',
                    data=dict(
                        set1=9123,
                        set2=9018,
                        set3=9090), follow_redirects=True
                    )
            self.assertIn(b'9123', response.data)


class TestRedirects(TestBase):
    def test_redirect_to_workoutlog_when_submit_workout(self):
            self.client.post('/login',
                    data=dict(
                        username ="test",
                        password ="test"), follow_redirects=True)
            response = self.client.post('/workout',
                    data=dict(
                        set1=1,
                        set2=2,
                        set3=3))
            self.assertRedirects(response, '/log')
    def test_login_redirect_when_workouts(self):
        with self.client:
            response = self.client.get('workout')
            self.assertRedirects(response, "/login?next=%2Fworkout")

    def test_redirect_to_login_when_view_log_if_not_logged_in(self):
        with self.client:
            response = self.client.get('/log')
            self.assertRedirects(response, "/login?next=%2Flog")
    def test_redirect_to_workout_when_already_logged_in(self):
        with self.client:
                    self.client.post('/login',
                    data=dict(
                    username ="test",
                    password ="test"))
                    response = self.client.get('/login')
                    self.assertRedirects(response, '/workout')
                    


    def test_redirect_to_login_after_registering(self):
        with self.client:
            response = self.client.post('/register',
                data=dict(
                    username="test2",
                    password="test2",
                    confirm_password="test2",
                    level= 90)
                )
            self.assertRedirects(response, "/login")

   

