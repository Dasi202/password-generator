class User:
    """
    Class that generates new instances of user.
    """

    user_list = []

    def _init_(self,first_name,last_name,user_name,password):
        self.first_name = first_name
        self.last_name  = last_name
        self.user_name = user_name
        self.password = password