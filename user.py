import random
import string 

class User:
    """
    Class that generates new instances of users
    """

    user_list = []

    def __init__(self, first_name, last_name, user_name, password):
        """
        Initialize method that helps us define properties for our objects
        """
        self.first_name = first_name
        self. last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        Method that saves user
        """
        User.user_list.append(self)

    @classmethod
    def user_exist(cls, username):
        """
        Method that checks if the user exists and returns a boolean
        """

        for user in cls.user_list:
            if user.user_name == username:
                return True

        return False

    @classmethod
    def check_user(cls, username, password):
        """
        Method that searches for user
        """
        current_user = ''
        for user in cls.user_list:
            if(user.user_name == username and user.password == password):
                current_user = user.username
            return current_user    

    @classmethod
    def verify_user(cls, username, password):
        """
        Method verifying the user
        """
        auth_user = ""
        for user in cls.user_list:
            if(user.user_name == username and user.password == password):
                auth_user = user.username
        return auth_user

    @classmethod
    def generatePassword(cls, stringLength):
        """
        Generate a random password string of letters and digits and special characters
        """
        password = string.ascii_uppercase + \
            string.ascii_lowercase + string.digits + "!@#$%&"
        return ''.join(random.choice(password) for i in range(stringLength))
   