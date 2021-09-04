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

def 
