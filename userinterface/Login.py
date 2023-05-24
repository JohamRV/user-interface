import random
import time
import os
from userinterface.Member import Member
from userinterface.Administrator import Administrator

ADMIN_LIST = [ "jromucho" ]
USER_LIST = [ "usuario" ]

class Login:
    @staticmethod
    def menu():

        while True:
            username = input("[.] Username: ")
            password = input("[.] Password: ")

            # Authentication
            if Login.valid_credential(username, password):
                print(f"\n[.] Welcome {username} to PucpStack!")
                
                role = Login.get_username_role(username)

                # Authorization
                if role == "member":
                    Member.menu()
                elif role == "administrator":
                    Administrator.menu()
    
                break
            else:
                print("\n[.] Credenciales inválidas. Intente de nuevo.")
                time.sleep(2)

    @staticmethod
    def valid_credential(username, password):
        # credential must be validate
        # here must be called the authentication method
        # TEMPORALLY
        if username in ADMIN_LIST or username in USER_LIST:
            return True
        else:
            return False
    
    @staticmethod
    def get_username_role(username):
        # this method must be use to request the user role only if the user
        # was authenticated
        if username in ADMIN_LIST:
            return "administrator"
        elif username in USER_LIST:
            return "member"