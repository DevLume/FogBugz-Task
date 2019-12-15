#!usr/bin/env python3
import json

class SuccesfulResponse(json.JSONEncoder):
    def __init__(self):
        self.userEmail = ""
        self.userLicense =  ""
        self.userReports = []