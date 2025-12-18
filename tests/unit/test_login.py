import unittest
from src.login import login

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(login("admin", "1234"), "Login successful")

    def test_wrong_password(self):
        self.assertEqual(login("admin", "1111"), "Invalid credentials")

    def test_empty_username(self):
        self.assertEqual(login("", "1234"), "Fields cannot be empty")

    def test_empty_password(self):
        self.assertEqual(login("admin", ""), "Fields cannot be empty")

if __name__ == "__main__":
    unittest.main()
