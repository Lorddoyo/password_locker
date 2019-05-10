class User:
    users_list = []
    '''
    Class that generates new instances of contacts 
    '''
    def __init__(self, username, email, password, credentials):
        '''
        function to intialize class
        '''
        self.uname = username
        self.email = email
        self.pword = password
        self.credentials = []



    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.users_list.append(self)
        
        
    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.users_list.remove(self)

    def find_user(self, uname):
        '''
        Function that check if a user exists with that username and return a Boolean
        '''
        
        listdata = User.users_list
        for item in listdata:
            if uname in item['uname']:
                return item
