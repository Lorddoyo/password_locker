#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
new_user = User('','','',[])

def create_user():
    '''
    Function to create a new user
    '''
    print('******** create account *******\n')
    username = input('Enter username__: \n')
    email = input('Enter email__: \n')
    password = input('Enter passoword__: \n')
    conf_pass = input('Retype password__: \n')

    result = checkNulls([username,email,password,conf_pass])
    if result:

        if password == conf_pass:
            new_user = User(username, email, password,[])
            new_user.save_user()
            print(new_user.uname)

def checkNulls(*args):
    result = all(item != '' for item in args)
    return result


def del_user(user):
    '''
    Function that finnds a user by
    '''
    new_user.delete_user()


def get_all_users():

    '''
    '''



    


def find_by_username(uname):
    '''
    Function that finds a contant by number and returns the user
    '''
    return new_user.find_user(uname)

def find_by_account(self, name):

    '''
    find_by_account method takes a searched account name and returns account credentials of that account.
    Args:
        account: Account name to search for
    Returns :
        Credentials of the user account that matches the searched account.
    '''

    for account in self.credentials_list:
        if account.account_name == name:
            return account

def login():
    '''
    '''
    print('*************** login *************\nEnter Username__ : \n')
    uname = str(input())
    result = checkNulls([uname])
    if result:
        account = find_by_username(uname)
        print('Enter password for {}\n'.format(uname))
        password = input()
        if password == account.pword:
            while True:
                print('**** you are currently loged in as {} *****\n'.format(uname))
                print('**** what would you like to do *****\ntype "e" to sign out, type "l" to list credentials, type "a" to add credentials\n')
                choices = input()
                if choices == 'e':
                    print('Successfuly loged out.\n\n')
                    break
                elif choices == 'l':
                    if account.credentials:
                        print('**** your currently stored accounts are as listed. *****\n')
                        for item in account.credentials:
                            print (' - your {} account under username {} and email {} password is secure.\n'.format( item.account_name, item.account_user_name ,item.account_email ))
                    else:
                        print('*** you have no account registered yet. want to add some? \nY/n***')
                        choice = input()
                        if choice == 'y':
                            while True:
                                acc_name = input('Enter account name__ : ')
                                acc_uname = input('Enter user name__ : ')
                                acc_email = input('Enter account email__ : ')
                                acc_password = input('Enter account password__ : ')

                                confNulls = checkNulls([acc_email,acc_name,acc_password,acc_uname])
                                if confNulls:
                                    new_credential = Credentials(acc_name,acc_uname,acc_email, acc_password)
                                    account.credentials.append(new_credential)
                                    print('your {} account has been successfully saved.\n'.format(acc_name))
                                    break
        else:
            print('wrong password')








def main():
    while True:
        if User.users_list:
            print('**** seems like there are available users ****\n\nWhat would you like to do? \ntype "l" for login, type "s" for signup')
            choice = input('choice\t')
            if choice=='l':
                login()
            elif choice=='s':
                create_user()
        else:
            print('***** No available users yet. sign up first *****')
            create_user()

if __name__ == '__main__':
    main()

   