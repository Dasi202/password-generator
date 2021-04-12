import unittest
from user import User
import pyperclip


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    """

    def tearDown(self):
        """
        It resets the user_list array(cleans up)
        """
        User.user_list = []

    def setUp(self):
        """
        It creates a test User
        """

        self.new_user = User("Danlon", "Situma", "Dasi202", "passcode")

    def test_init(self):
        """
        Test case to test if the object id initialized properly
        """
        self.assertEqual(self.new_user.first_name, "Danlon")
        self.assertEqual(self.new_user.last_name, "Situma")
        self.assertEqual(self.new_user.user_name, "Dasi202")
        self.assertEqual(self.new_user.password, "passcode")

    def test_save_user(self):
        """
        Test case to test if the user object is saved into the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()