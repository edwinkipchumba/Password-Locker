import random
import pyperclip

class User:
    ''''
    class that create a new user
    '''
    data_user = []

    def __init__(self, owner, key):
      ''''
      method to initialize user object
      '''
      self.owner = owner
      self.key = key

    def save_user(self):
       ''''
       method to save user object
       '''
       User.data_user.append(self)

class Credentials:
    '''
    class that creates new account credentials
    '''
    account_credentials=[] # list of accounts

    def __init__(self, account_name, username, password = None):
        '''
        method to initialize account object
        '''
        self.account_name = account_name
        self.username = username
        self.password = password if password else Credentials.password_generate()

    def save_account(self):
        '''
        method to save account object
        '''
        Credentials.account_credentials.append(self)

    def delete_account(self):
        '''
        method to delete an account
        '''
        Credentials.account_credentials.remove(self)