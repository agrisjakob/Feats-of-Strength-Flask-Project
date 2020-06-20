import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app import app, db, bcrypt
from app.models import Users, Exercises, ExercisesInWorkout, Workout

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_URI'),
                SECRET_KEY=getenv('TEST_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True)
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

        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("selenium1")
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("test")
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
        "test")
        self.driver.find_element_by_xpath('//*[@id="level"]').send_keys("90")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('login') in self.driver.current_url

        if __name__ == '__main__':
            unittest.main(port=5000)
