import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("Github", "https://github.com/Dasi202", "Dasi202", "pin")

    def test_init(self):
        self.assertEqual(self.new_credential.title, "Github")
        self.assertEqual(self.new_credential.url, "https://github.com/Dasi202")
        self.assertEqual(self.new_credential.user_name, "Dasi202")
        self.assertEqual(self.new_credential.password, "pin")
