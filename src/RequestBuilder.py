#!usr/bin/env python3

import collections
import json
from queryProperties.DateOpenedProperty import dateOpened
from queryProperties.RatingProperty import rating
from queryProperties.CategoryProperty import category
from QueryBuilder import QueryBuilder

from copy import copy

class RequestBuilder():
    def __init__(self, queryBuilder: QueryBuilder):
        self.queryBuilder = queryBuilder
        pass 

    def filterInputJSON(self, data: dict(), wantedKeys: set()) -> dict():
        if not('userEmail' in data) and not('correspondent' in data):
            print("Missing Correspondent in the input json. aborting")
            return (False, None)
        elif 'userEmail' in data:
            data['correspondent'] = data['userEmail']
            del data['userEmail']

        dictFilter = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        
        data = dictFilter(data, wantedKeys)

        return data
    
    def formSearchString(self, inputJSON: dict) -> str:        
        baseQueryParameters = set()

        tempJSON = copy(inputJSON)
        del tempJSON['correspondent'] # removing correspondent field from temporary json since it was checked previously.
        keys = tempJSON.keys()

        for key in keys:
            # getting class instance based on it's name string
            ctor = globals()[key]
            instance = ctor(inputJSON)
            baseQueryParameters.add(instance.__class__) # adding base property class instance

        query = self.queryBuilder.buildQuery(baseQueryParameters, inputJSON) # building a query with needed properties
          
        return query.toString()
