import unittest
import time
from flask import url_for
from urllib.request import urlopen
from flask_login import login_user, current_user, logout_user, login_required
from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app import app, db, bcrypt
from app.models import Users, Exercises, ExercisesInWorkout, Workout

testUser = 'test'
testPass = 'test'
testLevel = 90

class TestBase(LiveServerTestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TESTING_URI'),
                SECRET_KEY=getenv('TESTING_KEY'))
        return app

    def setUp(self):

        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/agrisjakob/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
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

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)



class TestRegistration(TestBase):

    def test_registration(self):
        self.driver.find_element_by_xpath("/html/body/a[4]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(testUser)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(testPass)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
        "test")
        self.driver.find_element_by_xpath('//*[@id="level"]').send_keys(testLevel)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('login') in self.driver.current_url
        assert Users.query.filter_by(userid=1).first().username == testUser

    
    def test_updating_workout_reps(self):
        self.driver.find_element_by_xpath("/html/body/a[4]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(testUser)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(testPass)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(testPass)
        self.driver.find_element_by_xpath('//*[@id="level"]').send_keys(testLevel)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        

        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(testUser)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(testPass)
        self.driver.find_element_by_xpath('//*[@id="remember"]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        
        
        time.sleep(1)
        self.driver.get("http://localhost:5000")
        
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="set1"]').send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="set2"]').send_keys(2)
        self.driver.find_element_by_xpath('//*[@id="set3"]').send_keys(3)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(2)
        assert ExercisesInWorkout.query.filter_by(workoutid=1).first().reps_completed == 1    
        assert url_for('log') in self.driver.current_url   

    
    
    
    
    
    if __name__ == '__main__':
            unittest.main(port=5000)


class TestUpdateWorkout(TestBase):

    def test_updating_previous_workout(self):
        self.driver.find_element_by_xpath("/html/body/a[4]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(testUser)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(testPass)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(testPass)
        self.driver.find_element_by_xpath('//*[@id="level"]').send_keys(testLevel)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)


        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(testUser)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(testPass)
        self.driver.find_element_by_xpath('//*[@id="remember"]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()


        time.sleep(1)
        self.driver.get("http://localhost:5000")

        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="set1"]').send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="set2"]').send_keys(2)
        self.driver.find_element_by_xpath('//*[@id="set3"]').send_keys(3)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(2)

        self.driver.find_element_by_xpath('/html/body/form/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="set1"]').send_keys(7)
        self.driver.find_element_by_xpath('//*[@id="set2"]').send_keys(7)
        self.driver.find_element_by_xpath('//*[@id="set3"]').send_keys(7)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        assert url_for('log') in self.driver.current_url
        assert ExercisesInWorkout.query.filter_by(workoutid=1).first().reps_completed == 7
