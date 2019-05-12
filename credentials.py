class Credentials:
    '''
    Class that generates new instances of user application credentials
    '''


    def __init__(self, account_name, account_user_name, account_email, account_password):
        '''
        __init__ method that defines properties for our credentials objects.
        '''

        self.account_name = account_name
        self.account_user_name = account_user_name
        self.account_email = account_email
        self.account_password = account_password

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved user from the user_list
        '''
        Credentials.delete_credentials(self)

    def add_credentials(self):
        '''
        '''

        Credentials.add_credentials(self)


