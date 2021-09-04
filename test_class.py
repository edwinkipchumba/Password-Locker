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
            lock_key = input()
        if not lock_key:
            print("Please provide correct details")

        else:
            save_user(create_user(lock_owner, lock_key))
            print("-"*10)
            print(f"{lock_owner}, Please enter your password again to login.")
            confirm = input()

        if confirm == lock_key:
            print("\n You are successfully logged in!")
            while True:
                print("-"*10)
                print("what would you like to do today? \n Use these short codes : \n\t\t aa - Add an account using your own words \n\t\t ga - Generate a password for your new account \n \t\t da - Display saved accounts \n \t\t sa -Search for an account \n \t\t d - Delete an account \n \t\t ex - Exit the password locker")
                short_code = input().lower()

                if short_code == "aa":
                    print("-"*10)
                    print("Enter an existing account")
                    print("Account name...(e.g: Facebook)")

                    # account

