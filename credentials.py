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


    # def display_all_accounts(self):
    #      '''
    #     display_all_accounts method returns the credentials list
    #     '''

    #     return Credentials.credentials_list

   
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