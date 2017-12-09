import unittest
from app import views

class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        self.username = "John"
        self.password = "Doe"
        self.id = "123456789"
        self.role = 1

    def tearDown(self):
        del self.username
        del self.password
        del self.id
        del self.role

    def test_athentication_with_out_id(self):
        return self.app.post('/login', data=dict(
            username = self.username,
            password = self.password,
        ), follow_redirects = True)


if __name__ == "__main__":
    unittest.main()
