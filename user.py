class User:
    users_list = []
    '''
    Class that generates new instances of contacts 
    '''
    def __init__(self, username, email, password):
        '''
        function to intialize class
        '''
        self.uname = username
        self.email = email
        self.pword = password


    def createUser(self, uname, email, pword):
        '''
        Function to create new user

        '''
        new_user = User( uname, email, pword)
        return new_user