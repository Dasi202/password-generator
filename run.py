#!/usr/bin/env python3.8
from user import User
from credential import Credential

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

def main():
        print("'Hello Welcome to password generator.\n Use one of these short codes to continue:\n su - Sign Up\n li - Log in")
        short_code = input().lower ()
        if short_code == 'su':
            print("Sign Up")
            print("-"*10)
            first_name = input("First name: ")
            last_name = input("Last name: ")
            user_name = input("Username: ")
            while True:
                print("kp - To Key in Password \n gp - To Generate Password")
                pwd_option = input().lower()
                if pwd_option == 'kp':
                    password = input("Enter your password\n")
                    break
                elif pwd_option == 'gp':
                    length = input("How many characters should your password entail?")
                    int_length = int(length)
                    password = generate_password(int_length)
                    break
                else:
                    print("Password option invalid please try again")
            save_users(create_user(first_name, last_name,user_name,password))
            print("-"*20)
            print(f"Hello {user_name}, welcome to password generator! Your password is {password}")
        elif short_code == "li":
            print("-"*10)
            print("Enter your username and password to Log in")
            print("-"*10)
            username = input("Username:")
            password = input("Password:")
            login = verify_users(username, password)
            if verify_users == login:
                print (f"Hello {username}.Welcome to password generator\n")
        while True:
            print("Use these short codes:\n cc - Create a new credential\n dc - Display credential\n fc - Find credentials \n gp - Generate a random password d- Delete credentials \n ex - Exit the application \n")
            short_code == input().lower()
            if short_code == "cc":
                print("Create credential")
                print("*="*10)
                print("Enter Title eg .. Gmail")
                title = input().lower
                print("Enter URL eg .. https://www.gmail.com/login")
                url = input().lower().strip()
                print("Enter username...")
                user_name = input()
                print(user_name)
                while True:
                    print("Enter: \n kp - To key in password or \n gp - To generate password")
                    pwd_choice = input().lower()
                    if pwd_choice == "kp":
                        pwd = input("Key in your password...\n")
                        break
                    elif pwd_choice == "gp":
                        length = int(input("How many characters should your password entail?"))
                        int_length = int(length)
                        pwd = generate_password(int_length)
                        break
                    else:
                        print("Invalid choice Please try again")
                save_credentials(create_credential(title, url, user_name, pwd))
                print(f"credential for {title}: \n URL: {url} \n Username: {user_name}\n Password: {pwd}\n")
            elif s_code == "dc":
                if display_credentials():
                    print("Displaying crredentials")
                    print("*="*15)
                    for credential in display_credentials():
                        print(f"Title:{credential.title}\n URL: {credential.url}\n Username: {credential.user_name}\n password: {credential.password}")
                        print("*="*15)
                else:
                    print("Credential is yet to be saved..\n")
            elif s_code == "fc":
                search_name = input("Enter account title to search for ").lower().strip()
                if find_credentials(search_name):
                    search_credential = find_credentials(search_name)
                    print("*="*25)
                    print(f"Title: {search_credential.title}\n URL: {search_credential.url}\n Username: {search_credential.user_name} \n Password: {search_credential.password}")
                    print("*="*25)
                else:
                    print("Credential does not exist\n")
            elif s_code == "d":
                search_name = input("Enter title of credential you want to delete")
                if find_credentials(search_name):
                    print("*_"*25)
                    print(f"credentials for {search_credential.title} heve been deleted successfully")
                else:
                    print("Credential does not exist \n")

            elif s_code == "gp":
                length = int(
                    input("please enter the lenght of the password you want generated..."))
                int_length = int(length)
                pwd = generate_password(int_length)
                print(f"generated password: {pwd}")
            elif s_code == "ex":
                print("Thanks for using Password Locker....")
                break
            else:
                print("Wrong entry... Check your entry again and let it match those in the menu")
        else:
            print("Please enter a valid input to continue")


if __name__ == '__main__':
    main()
