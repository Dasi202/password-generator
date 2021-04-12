#!/usr/bin/env python3.8
def create_user(fname, lname, uname, pwd):
    """
    Function creating a new user
    """
    new_user = User(fname, lname, uname, pwd)
    return new_user

def save_users(user):
    """
    Function to save user
    """
    user.save_user()

def delete_users(user):
    '''
    Function to delete user
    '''
    user.delete_user()


def display_users():
    '''
    Function to display users
    '''
    return User.display_users()


def create_credential(title, url, uname, pwd):
    '''
    Function creating a new credential
    '''
    new_credential = Credential(title, url, uname, pwd)
    return new_credential


def save_credentials(credential):
    '''
    Function saving credentials
    '''
    credential.save_credential()


def delete_credentials(credential):
    ''''
    Function deleting credentials
    '''
    credential.delete_credential()


def display_credentials():
    '''
    Function displaying credentials
    '''
    return Credential.display_credentials()


def find_credentials(title):
    '''
    Function finding credentials
    '''
    return Credential.find_by_title(title)
