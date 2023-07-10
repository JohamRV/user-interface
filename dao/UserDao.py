import requests
import json

API_GATEWAY = "localhost:8081"
BASE_URL = "http://" + API_GATEWAY 

class UserDao:
    
    def __init__(self) -> None:
        self.url = BASE_URL + "/ms-user"
        pass

    def list_users(self):
        pass

    def create_user(self):
        pass

    def edit_user(self):
        pass

    def delete_user(self):
        pass