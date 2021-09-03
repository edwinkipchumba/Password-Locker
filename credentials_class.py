import unittest
import pyperclip
from user_class import Credentials
from user_class import User

# sub-class
class UserTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each user test
        '''
        self.new_user = User("James", "Doe")