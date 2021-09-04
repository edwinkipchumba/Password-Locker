#!

from user_class import Credentials
from user_class import User

def create_user(lock_owner, lock_key):
        '''
        function to create a new user
        '''
        new_user = User(lock_owner, lock_key)
        return new_user