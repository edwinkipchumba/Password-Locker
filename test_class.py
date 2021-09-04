#!

from user_class import Credentials
from user_class import User

def create_user(lock_owner, lock_key):
        '''
        function to create a new user
        '''
        new_user = User(lock_owner, lock_key)
        return new_user

def save_user(data):
    '''
    function to save a new user
    '''
    data.save_user()

def create_account(account, u_name, passwd):
    '''
    function to create a new account
    '''
    new_account = Credentials(account, u_name, passwd)
    return new_account

def save_accounts(credentials):
    '''
    function to save the new account
    '''
    credentials.save_account()

def delete_accounts(credentials):
    '''
    function to delete an account
    '''
    credentials.delete_account()

def search_accounts(search):
    '''
    function to find an account by account name
    '''
    return Credentials.search_accounts(search)
def generate_password():
    '''
    function to generate a password
    '''
    random_password = Credentials.password_generate()
    return random_password

def display_account():
    '''
    function to display all accounts saved
    '''
    return Credentials.display_accounts()

def main():
    print("")
    print("")
    print("")
    print("")
    print("")

    print("\nHello and welcome!")
    print("\n 1. Create an account  \n 2. Exit app")
    option = input()

    if option == '1':
        print("Enter your name")
        lock_owner = input()
        if not lock_owner:
            print("Please enter your encrypting details")
            
        else:
                print("Enter your password")

