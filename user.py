class User:
    """
    Class that generates new instances of users
    """

    user_list = []

    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self. last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def user_exist(cls, username):

        for user in cls.user_list:
            if user.user_name == username:
                return True

        return False

   