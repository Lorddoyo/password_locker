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

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.users_list.append(self)

    def delete_contact(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    

    