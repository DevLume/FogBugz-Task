#!usr/bin/env python3

from Credentials import Credentials
from json import JSONEncoder
from ResponseManager import ComplexEncoder
import json
import http.client 
import base64
from ResponseManager import SuccesfulResponse, Report, ErrorResponse

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
            "password": base64.b64decode(credentials.password).decode()
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
    def testRequest(self, token, query) -> None:
        print("test request...")

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
        l = json.loads(response.read())
        print(self.formResponse(l))
    
    def formResponse(self, data) -> str:
        #Temporary solution. rework later TODO
        resp = SuccesfulResponse()
        resp.userEmail = data['data']['cases'][0]['sCustomerEmail']
        resp.userLicense = data['data']['cases'][0]['license']
        for case in data['data']['cases']:
            rep = Report()
            rep.id = case['ixBug']
            rep.title = case['sTitle']
            rep.dateOpened = case['dtOpened']
            rep.dateClosed = case['dtClosed']
            rep.category = case['sCategory']
            rep.status = case['sStatus']
            rep.rating = case['rating']
            rep.version = case['sVersion']
            resp.userReports.append(rep.__dict__)

        respJSON = json.dumps(resp, cls=ComplexEncoder)
        
        #print(resp.__dict__)

        #encoder = JSONEncoder()
        #respJSON = encoder.encode(resp.__dict__)

        print(json.dumps(respJSON, indent=4, sort_keys=False))