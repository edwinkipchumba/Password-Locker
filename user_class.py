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