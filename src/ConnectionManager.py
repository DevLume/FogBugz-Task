#!usr/bin/env python3

from Credentials import Credentials
from json import JSONEncoder

import json
import http.client 
import base64

from ResponseBuilder import ResponseBuilder

class ConnectionManager():
    def __init__(self):
        self.responseBuilder = ResponseBuilder()
        pass 

    #login, return token
    def login(self, credentials: Credentials) -> (bool, dict()):
        print("Sending login request...")
        conn = http.client.HTTPSConnection("fogbugz.unity3d.com")
        
        headers = {'Content-type': 'application/json'}

        cred = {
            "cmd": "logon",
            "email": credentials.email,
            "password": base64.b64decode(credentials.password).decode()
        }
        
        jsonCred = json.dumps(cred)

        conn.request('POST', "/f/api/0/jsonapi", jsonCred, headers)

        response = conn.getresponse()
        data = json.loads(response.read())
        if(len(data['errors']) > 0):
            print("Errors are found when logging in!")
            return (False, self.responseBuilder.buildResponse(data))
        else:
            token = data['data']['token']
            return (True, token)
    
    def logoff(self, token) -> None:
        print("Sending logoff request...")

        conn = http.client.HTTPSConnection("fogbugz.unity3d.com")
        
        headers = {'Content-type': 'application/json'}

        cred = {
            "cmd": "logoff",
            "token": token,
        }
        
        jsonCred = json.dumps(cred)

        conn.request('POST', "/f/api/0/jsonapi", jsonCred, headers)

        response = conn.getresponse()
        data = json.loads(response.read())
        if(len(data['errors']) > 0):
            print("Errors are found when logging off!")
            return (False, self.responseBuilder.buildResponse(data))
        else:
            return (True, "")

    def sendQuery(self, token, query) -> dict:
        print("Sending query...")

        conn = http.client.HTTPSConnection("fogbugz.unity3d.com")
        
        headers = {'Content-type': 'application/json'}

        body = {
            "cmd": "search",
            "token": token,
            "q": query,
            "cols": [
                "ixBug", 
                "sTitle", 
                "sCategory",
                "sVersion",
                "sCustomerEmail", 
                "dtOpened", 
                "dtClosed", 
                "sStatus",
                "ixStatus",
                "rating",
                "license"        
            ] 
        }
        
        jsonBody = json.dumps(body)

        conn.request('POST', "/f/api/0/jsonapi", jsonBody, headers)

        response = conn.getresponse()
        data = json.loads(response.read())

        return self.responseBuilder.buildResponse(data)