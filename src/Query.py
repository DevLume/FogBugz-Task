#!usr/bin/env python3

# class names are dictated by the properties in the search json files
# this allows to call them using reflection

class dateOpened():
    def __init__(self, queryJSON):
        self.dateOpened = queryJSON['dateOpened']

    def toString(self) -> str:
        retStr = "opened: "
        if("dateFrom" in self.dateOpened):
            retStr += self.dateOpened['dateFrom']+".."
        else:
            retStr += ".."
        
        if("dateTo" in self.dateOpened):
            retStr += self.dateOpened['dateTo']

        return retStr

class rating():
    def __init__(self, queryJSON):
        self.rating = queryJSON['rating']

    def toString(self) -> str:
        retStr = "rating: "
        if("ratingFrom" in self.rating):
            retStr += str(self.rating['ratingFrom'])+".."
        else:
            retStr += ".."
        
        if("ratingTo" in self.rating):
            retStr += str(self.rating['ratingTo'])
    
        return retStr

class category():
    def __init__(self, queryJSON):
        self.category = queryJSON['category']

    def toString(self) -> str:
        return self.category
