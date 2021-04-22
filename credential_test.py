import unittest
import pyperclip
from credential import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours.
    """
    def tearDown(self):
        Credential.credential_list = []


    def setUp(self):
        self.new_credential = Credential("Github", "https://github.com/Dasi202", "Dasi202", "pin")

    def test_init(self):
        """
        Test case to test if the object id is initialized properly
        """
        self.assertEqual(self.new_credential.title, "Github")
        self.assertEqual(self.new_credential.url, "https://github.com/Dasi202")
        self.assertEqual(self.new_credential.user_name, "Dasi202")
        self.assertEqual(self.new_credential.password, "pin")

    def test_save_credential(self):
        """
        Test case to test if the credential object is saved into the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        """
        Test case to check if we can save multiple credential objects to the credential list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        """
        Test case to check if the saved credential can be deleted
        """
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_title(self):
        """
        Test case to check if credential can be find by title
        """
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        found_credential = Credential.find_by_title("Gmail")
        self.assertEqual(found_credential.title, test_credential.title)

    def test_credential_exists(self):
        """
        Test case to check if credential exists
        """
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("Gmail")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        """
        Test case that displays all the saved credentials
        """
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    
if __name__ == '__main__':
    unittest.main()

