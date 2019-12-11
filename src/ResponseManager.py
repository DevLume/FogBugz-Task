#!usr/bin/env python3

import json

class ComplexEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, SuccesfulResponse):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

class SuccesfulResponse(json.JSONEncoder):
    def __init__(self):
        self.userEmail = ""
        self.userLicense =  ""
        self.userReports = []

class Report():
    def __init__(self):
        self.id = 0
        self.title = ""
        self.dateOpened = ""
        self.dateClosed = ""
        self.category = ""
        self.status = ""
        self.rating = 0
        self.version = ""

class ErrorResponse():
    def __init__(self):
        pass 

