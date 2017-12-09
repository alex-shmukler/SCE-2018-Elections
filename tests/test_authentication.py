import unittest
from flask import Flask

app = Flask(__name__)

class AuthenticationTest(unittest.TestCase):

    def setUp(self):
        self.firstname = "John"
        self.lastname = "Doe"
        self.appp = app.test_client()

    def tearDown(self):
        del self.firstname
        del self.lastname


    def athentication_with_out_id(self):
        return self.appp.get('/login', data=dict(
            first_name = self.firstname,
            last_name = self.lastname,
        ), follow_redirects = True)

    def test_login_with_out_id(self):
        rv = self.athentication_with_out_id()
        print (rv.data)
        assert("Enter all fields" in rv.data)

if __name__ == "__main__":
    unittest.main()
