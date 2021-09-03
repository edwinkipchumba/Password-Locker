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

    @classmethod
    def password_generate(cls):
        '''
        class method to generate random password
        '''
        password_length =8
        possible_characters = "@abcdefghijklmnopqrstuvwxyz-1234567890&ABCDEFGHIJKLMNOPQRSTUVWXYZ!"
        random_character = [random.choice(possible_characters) for i in range(password_length)]
        auto_password = "".join(random_character)
        return auto_password

    @classmethod
    def display_accounts(cls):
        '''
        class method to display all accounts
        '''
        return cls.account_credentials
       
    @classmethod
    def search_accounts(cls, search):
        '''
        class method to search for an account 
        '''
        for acc in cls.account_credentials:
            if acc.account_name == search:
                return acc

    @classmethod
    def copy_password(cls):
        '''
        method to copy passwords
        '''
        for acc in cls.account_credentials:
            pyperclip.copy(acc.password)
            pyperclip.paste()