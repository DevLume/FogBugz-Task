#!usr/bin/env python3

from responseProperties.Error import Error
from responseProperties.ErrorResponse import ErrorResponse
from responseProperties.Report import Report
from responseProperties.SuccesfulResponse import SuccesfulResponse

import json

from ComplexEncoder import ComplexEncoder

class ResponseBuilder():
    def __init__(self):
        pass 

    def buildResponse(self, data: dict()) -> dict():
        resp = None
        if(len(data['errors']) > 0):
            resp = ErrorResponse()
            for error in data['errors']:
                e = Error()
                e.message = error['message']
                e.detail = error['detail']
                e.code = error['code']
                resp.errors.append(e.__dict__)
        else:
            resp = SuccesfulResponse()
            for case in data['data']['cases']:
                if(resp.userEmail == "" and resp.userLicense == ""):
                    resp.userEmail = data['data']['cases'][0]['sCustomerEmail']
                    resp.userLicense = data['data']['cases'][0]['license']
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

        return resp.__dict__      
            