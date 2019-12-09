#!usr/bin/env python3

from FileManager import FileManager
from RequestFormer import RequestFormer
from Credentials import Credentials
from ConnectionManager import ConnectionManager

if __name__ == "__main__":
    fm = FileManager()

    wantedKeys = {"userEmail", "dateOpened", "rating", "category"} # a set of properties used to filter the input JSON

    data = fm.readJSON("../InputFiles/test1.json")

    rf = RequestFormer()

    data = rf.filterInputJSON(data, wantedKeys) # making sure that our Input JSON contains only needed properties 

    #print(data)

    cm = ConnectionManager()

    token = cm.login(Credentials("", ""))

    cm.testRequest(token, data)

    cm.logoff(token)

    #print(data)