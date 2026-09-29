from User import *
class Admin(User):
   def __init__(self,user_id, name, email, remove_access):
        super().__init__(user_id, name, email) 
        self.remove_access = remove_access