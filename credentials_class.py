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
        self.assertEqual(len(User.data_user),1)

class User_classTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each test
        '''
        self.new_account = Credentials("instagram","Mary","myPassword")

    def tearDown(self):
        '''
        method run fter each test
        '''
        Credentials.account_credentials = []

    def test_init(self):
        '''
        test to check for proper initialization
        '''
        self.assertEqual(self.new_account_name,"instagram")
        self.assertEqual(self.new_account.username,"Mary")
        self.assertEqual(self.new_account.password,"myPassword")

    def test_save_account(self):
        '''
        test method that checks if account has been saved
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.account_credentials),1)

    def test_save_multiple(self):
        '''
        test method to check if user can add many accounts
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Edu", "Kenya@123")
        another_account.save_account()
        self.assertEqual(len(Credentials.account_credentials),2)

    def test_delete_account(self):
        '''
        test method to check if an account has been deleted
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Edu", "Morgan")
        another_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_credentials),1)

    def test_password_autogenerate(self):
        '''
        test method to test auto generation of passwords
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Edu")
        another_account.save_account()

    def test_display_accounts(self):
        '''
        test method to check displaying of accounts
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter","Chris", "Mulili")
        another_account.save_account()
        self.assertEqual(Credentials.display_accounts(), Credentials.display_accounts)

    def test_search_accounts(self):
        '''
        test method to test search functionality
        '''
        self.new_account.save_account()
        another_account =Credentials("Twitter", "Edu", "Kenya@123")
        another_account.save_account()
        self.assertEqual(another_account,Credentials.search_accounts("Twitter"))

if __name__ == '__main__':
    unittest.main