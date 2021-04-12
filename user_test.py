from user import User
import unittest

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        """
        It creates a test User
        """
        self.new_user = User ("Danlon", "Situma", "Dasi", "password")

    def test_init_(self):
        self.assertEqual(self.new_user.first_name, "Danlon")
        self.assertEqual(self.new_user.last_name, "Situma")
        self.assertEqual(self.new_user.user_name, "Dasi")
        self.assertEqual(self.new_user.password, "password")  

if __name__ == '__main__':
    unittest.main()       