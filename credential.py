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
        Credential.credential_list.append(self)

    def delete_credential(self):
        Credential.credential_list.remove(self)
