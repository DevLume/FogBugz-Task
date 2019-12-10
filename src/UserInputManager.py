#!usr/bin/env python3

from Credentials import Credentials
from getpass import getpass
import base64

class UserInputManager():
    def __init__(self):
        self.Credentials = None
        pass 

    def getUserCredentials(self):
        print("Hello, please introduce yourself")

        email = input("e-mail:")
        password = base64.b64encode(getpass("password:").encode())

        return Credentials(email, password)
