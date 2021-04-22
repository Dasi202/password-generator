import pyperclip
import random
import string

class Credential:
    """
    Class that generates new credentials for users
    """
    credential_list = []

    def __init__(self, title, url, user_name, password):
        self.title = title
        self.url = url
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        """
        Method that saves the credential
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        Method that deletes credential
        """
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_title(cls, title):
        """
        Method finds credential via title
        """
        for credential in cls.credential_list:
            if credential.title == title:
                return credential

    @classmethod
    def credential_exist(cls, title):
        """
        Method checks if credential exists
        """
        for credential in cls.credential_list:
            if credential.title == title:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method dispalys the credentials
        """
        return cls.credential_list

    @classmethod
    def generatePassword(cls, stringLength):
        """
        Generate a 8 character random password string of letters and digits and special characters
        """
        password = string.ascii_uppercase + \
            string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))