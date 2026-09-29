from User import *
class Mentor(User):
    def __init__(self,user_id, name, email, expertise):
            super().__init__(user_id, name, email) 
            self.expertise = expertise