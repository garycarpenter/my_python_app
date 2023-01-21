"""this module creates displays and deletes user"""


class UserClass(object):
    """this class describes user"""

    def __init__(self, first_name, last_name, email_address, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.user_type = user_type

    def display_user(self):
        """displays user"""
        print(self.first_name)
        print(self.last_name)
        print(self.email_address)
        print(self.user_type)

    def __del__(self):
        print("You have deleted user. ")

print('Hello World!')
