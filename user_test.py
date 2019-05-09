import unittest
from user import User
import pyperclip


class TestUser(unittest.TestCase):
    '''
    Test clasnew_contactnew_contacts defines test cases for the user class behaviours.

    Args:
    unittest.Testcase: Testcase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        '''
        self.new_user =User('Lorddoyo', 'john@gmail.com', 'damnn')
    def test_init(self):
        '''
        test_init test case to test if the object is intialized properly
        '''
        self.assertEqual(self.new_user.uname, 'Lorddoyo') 
        self.assertEqual(self.new_user.email, 'john@gmail.com')
        self.assertEqual(self.new_user.pword, 'damnn')
        
