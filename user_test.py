import unittest
from user import User



class TestUser(unittest.TestCase):
    '''
    Test clasnew_usernew_user defines test cases for the user class behaviours.

    Args:
    unittest.Testcase: Testcase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        '''
        self.new_user = User('Lorddoyo', 'john@gmail.com', 'damnn')

    def test_init(self):
        '''
        test_init test case to test if the object is intialized properly
        '''
        self.assertEqual(self.new_user.uname, 'Lorddoyo') 
        self.assertEqual(self.new_user.email, 'john@gmail.com')
        self.assertEqual(self.new_user.pword, 'damnn')
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into the user users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
    
    def tearDown(self):
        User.users_list=[]
        '''
        tearDown method that does clean up after class test case has run.
        '''
    
    def test_delete_user(self):
        '''
        delete_user method deletes a saved user from the users_list
        '''
        self.test_new_user = User('Lorddoyo', 'john@gmail.com', 'damnn')
        self.new_user.save_user()
        self.test_new_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.users_list),1)
        


    
    def test_user_exist(self):
        '''
        Method that a username and returns a user that matches a username.
        Args:
        username:username to search for.
        Returns:
        User of person that matches the number.
        '''
        self.new_user.find_user(self.new_user.uname)

        

if __name__ == '__main__':
    unittest.main()