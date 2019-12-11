#!usr/bin/env python3

import collections
import json
from Query import dateOpened
from Query import rating
from Query import category

from copy import copy

class RequestFormer():
    def __init__(self):
        pass 

    def filterInputJSON(self, data: dict(), wantedKeys: set()) -> dict():
        if not('userEmail' in data) and not('correspondent' in data):
            print("Missing Correspondent in the input json. aborting")
            return None
        elif 'userEmail' in data:
            data['correspondent'] = data['userEmail']
            del data['userEmail']

        dictFilter = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        
        data = dictFilter(data, wantedKeys)

        return data 
    
    def formSearchString(self, inputJSON) -> str:        
        baseQueryParameters = set()

        tempJSON = copy(inputJSON)
        del tempJSON['correspondent']
        keys = tempJSON.keys()

        for key in keys:
            ctor = globals()[key]
            instance = ctor(inputJSON)
            baseQueryParameters.add(instance.__class__)

        print((rating, category, dateOpened))
        print(baseQueryParameters)
        print(inputJSON)

        query = buildQuery(baseQueryParameters, inputJSON)
        
        print(query.toString())

        return query.toString()

    

def buildQuery(queryBases, queryJSON):
    class Query(*queryBases):
        def __init__(self, queryJSON, *base):
            self.body = "correspondent: "
            self.body += queryJSON['correspondent']
            for b in base:
                self.body += " and "
                b.__init__(self, queryJSON)
                self.body += b.toString(self)
        
        def toString(self) -> str:
            return self.body
    
    return Query(queryJSON, *queryBases)

    