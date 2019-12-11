#!usr/bin/env python3

from FileManager import FileManager
from RequestFormer import RequestFormer
from Credentials import Credentials
from ConnectionManager import ConnectionManager

from RequestFormer import buildQuery

from UserInputManager import UserInputManager

if __name__ == "__main__":
    fm = FileManager()

    wantedKeys = {"correspondent", "dateOpened", "rating", "category"} # a set of properties used to filter the input JSON

    data = fm.readJSON("../InputFiles/test1.json")

    #fm.writeJSON(data, "../OutputFiles/testOutput0.json")

    rf = RequestFormer()

    """data = rf.filterInputJSON(data, wantedKeys)
    rf.formSearchString(data)"""

    uim = UserInputManager()
    cred = uim.getUserCredentials()

    data = rf.filterInputJSON(data, wantedKeys)

    #print(data)

    query = rf.formSearchString(data)

    cm = ConnectionManager()

    token = cm.login(cred)

    cm.testRequest(token, query)

    cm.logoff(token)