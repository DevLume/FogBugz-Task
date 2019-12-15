#!usr/bin/env python3

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