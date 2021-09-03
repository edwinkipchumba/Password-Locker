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

    def tearDown(self):
        '''
        method called after each user test
        '''
        User.data_user = []

    def test_init(self):
        '''
        test method to check if user class is initialized correctly
        '''
        self.assertTrue(self.new_user.owner,"James")
        self.assertTrue(self.new_user.key, "Doe")

    def test_save_user():
        '''
        test method to test if user has been saved into class list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.data_user), 1)