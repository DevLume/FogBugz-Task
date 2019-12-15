#!usr/bin/env python3

import json

class ComplexEncoder(json.JSONEncoder):
    #TODO: rework isinstance check
    def encode(self, obj):
        """if isinstance(obj, #SuccesfulResponse):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)"""
        pass