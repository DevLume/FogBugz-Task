#!usr/bin/env python3

import collections
import json

class RequestFormer():
    def __init__(self):
        pass 

    def filterInputJSON(self, data: dict(), wantedKeys: set()) -> dict():
        if not('userEmail' in data):
            print("Missing userEmail")
            return None

        dictFilter = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        
        data = dictFilter(data, wantedKeys)

        return data  
    