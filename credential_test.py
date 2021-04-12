import unittest
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
        self.assertEqual(self.new_credential.title, "Github")
        self.assertEqual(self.new_credential.url, "https://github.com/Dasi202")
        self.assertEqual(self.new_credential.user_name, "Dasi202")
        self.assertEqual(self.new_credential.password, "pin")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_title(self):
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        found_credential = Credential.find_by_title("Gmail")
        self.assertEqual(found_credential.title, test_credential.title)

    def test_credential_exists(self):
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "https://gmail.com/signup/", "situwali", "google")
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("Gmail")
        self.assertTrue(credential_exists)
        
if __name__ == '__main__':
    unittest.main()

