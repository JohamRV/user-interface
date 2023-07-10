import requests
import json
API_GATEWAY = "localhost:8081"
BASE_URL = "http://" + API_GATEWAY 

class SliceDao:

    def __init__(self) -> None:
        self.url = BASE_URL + "/ms-slice-manager"
        # self.token = token

    def create_slice(self, name:str, description:str):
        path = "/create"
        #headers={"Authorization":self.token}
        headers={"Content-Type": "application/json"}
        body={
            "slice":{
                "sliceName": name,
                "description": description
            }
        }
        response = requests.post(url=self.url + path, data=json.dumps(body), headers=headers)
        return response
    
    def edit_slice(self, sliceId:str, name:str, description:str):
        path = "/edit"
        #headers={"Authorization":self.token}
        headers={"Content-Type": "application/json"}
        body={
            "slice":{
                "sliceId": sliceId,
                "sliceName": name,
                "description": description
            }
        }
        response = requests.put(url=self.url + path, data=json.dumps(body), headers=headers)
        return response

    def assign_slice(self, userId:str, sliceId:str):
        path = "/assign/"+userId + "?sliceId=" + sliceId
        response = requests.post(url=self.url + path)
        return response

    def list_slices(self):
        path = "/list"
        #headers={"Authorization":self.token}
        response = requests.get(url=self.url + path)
        return response

    def delete_slice_by_id(self, sliceId:str):
        path = "/delete/" + sliceId
        #headers={"Authorization":self.token}
        response = requests.delete(url=self.url + path)
        return response

    def list_slices_by_id(self, sliceId:str):
        path = "/list-by-id/" + sliceId
        #headers={"Authorization":self.token}
        response = requests.get(url=self.url + path)
        return response

    def list_slice_by_username(self, username:str):
        path = "/list-by-username/" + username
        #headers={"Authorization":self.token}
        response = requests.get(url=self.url + path)
        return response
    