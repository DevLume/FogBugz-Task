#!usr/bin/env python3

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