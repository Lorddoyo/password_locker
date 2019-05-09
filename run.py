#!/usr/bin/env python3.6
from user import User 

def create_user(username,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(username, email, password)
    return new_user

def delete_user(user):
    '''
    Function that finnds a user by
    '''
    user.delete_user()

def save_user(user):
    '''
    Function to save user
    ''' 
    user.save_user()

def find_by_username(uname):
    '''
    Function that finds a contant by number and returns the user
    '''
    return User.find_user(uname)

def main():
    print('cows')
if __name__ == '__main__':
    main()

   