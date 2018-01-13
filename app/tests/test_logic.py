import unittest

import time
from selenium.webdriver.common.keys import Keys
from flask import Flask
from flask_testing import LiveServerTestCase
from app.models import User,Party
from app import app, db
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class SeleniumTest(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(app)
        with app.app_context():
            db.drop_all()
            db.create_all()
            self.init_db()
        return app

    def init_db(self):

        self.testUser = User('test', 'me',1234567800,0,0)
        self.party = Party('partyTest', 'https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg', 0)

        db.session.add(self.testUser)
        db.session.add(self.party)
        db.session.commit()

    def setUp(self):
         self.browser = webdriver.PhantomJS(executable_path="app/tests/phantomjs")
         self.browser.get(self.get_server_url())
         self.msg = 'The user is not registered!'
         self.msg2 = 'Your vote has been successfully recorded'


    # def test_registered_user(self):
    #     first_name = self.browser.find_element_by_id("first_name")
    #     first_name.send_keys("test")
    #
    #     last_name = self.browser.find_element_by_id("last_name")
    #     last_name.send_keys("me")
    #
    #     id_num = self.browser.find_element_by_id("id_num")
    #     id_num.send_keys(1234567800)
    #
    #     submit = self.browser.find_element_by_id("submit")
    #     submit.click()
    #
    #     assert self.msg not in self.browser.page_source
    #     self.browser.save_screenshot('registered_user.png')
    #
    #
    #
    # def test_unregistered_user(self):
    #     first_name = self.browser.find_element_by_id("first_name")
    #     first_name.send_keys("test1")
    #
    #     last_name = self.browser.find_element_by_id("last_name")
    #     last_name.send_keys("me1")
    #
    #     id_num = self.browser.find_element_by_id("id_num")
    #     id_num.send_keys(123456787)
    #
    #     submit = self.browser.find_element_by_id("submit")
    #     submit.click()
    #
    #     assert self.msg in self.browser.page_source
    #     self.browser.save_screenshot('unregistered_user.png')




    def test_registered_user_and_finish(self):
        browser = self.browser
        print(browser.title)
        first_name = self.browser.find_element_by_id("first_name")
        first_name.send_keys("test")

        last_name = self.browser.find_element_by_id("last_name")
        last_name.send_keys("me")

        id_num = self.browser.find_element_by_id("id_num")
        id_num.send_keys(1234567800)

        submit = self.browser.find_element_by_id("submit")
        submit.click()

        if self.msg not in self.browser.page_source:
            selectedParty = self.browser.find_element_by_id("partyTest")
            self.browser.execute_script("arguments[0].click();",selectedParty)
            browser.find_element_by_id('approve').click()
            browser.switch_to.active_element
            time.sleep(3)
            browser.find_element_by_id('ok').click()
            assert self.msg2 in self.browser.page_source


    def tearDown(self):
        self.browser.quit()
        with app.app_context():
            db.drop_all()
            db.session.remove()


if __name__ == '__main__':
    unittest.main()