#!usr/bin/env python3

from Credentials import Credentials
import json
import http.client 

class ConnectionManager():
    def __init__(self):
        pass 

    #login, return token
    def login(self, credentials: Credentials) -> str:
        print("Sending login request...")
        conn = http.client.HTTPSConnection("fogbugz.unity3d.com")
        
        headers = {'Content-type': 'application/json'}

        cred = {
            "cmd": "logon",
            "email": credentials.email,
            "password": credentials.password
        }
        
        jsonCred = json.dumps(cred)

        conn.request('POST', "/f/api/0/jsonapi", jsonCred, headers)

        response = conn.getresponse()
        l = json.loads(response.read())
        print(l)

        token = l['data']['token']
        return token
    
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
        l = json.loads(response.read())
        print(l)

    #TODO: Remove later
    def testRequest(self, token, InputJSON) -> None:
        print("test request...")

        conn = http.client.HTTPSConnection("fogbugz.unity3d.com")
        
        headers = {'Content-type': 'application/json'}

        body = {
            "cmd": "search",
            "token": token,
            "q": 'correspondent: "email"',
            "cols": "sTitle"
        }
        
        jsonBody = json.dumps(body)

        conn.request('POST', "/f/api/0/jsonapi", jsonBody, headers)

        response = conn.getresponse()
        l = json.loads(response.read())
        print(l)


