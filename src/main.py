#!usr/bin/env python3

from FileManager import FileManager
from Credentials import Credentials
from Configuration import Configuration
from ConnectionManager import ConnectionManager

from QueryBuilder import QueryBuilder

from RequestBuilder import RequestBuilder

from UserInputManager import UserInputManager

if __name__ == "__main__":
    uim = UserInputManager()
    config = uim.parseCLArgs() # parsing CL arguments may change the config
    credentials = uim.getUserCredentials() 

    fm = FileManager()
    inputData = fm.readJSON(config.inputFile)

    # Query builder may be different in the future, hence allowing RequestBuilder to use different Query builders
    qb = QueryBuilder()
    rq = RequestBuilder(qb)

    filteredInputData = rq.filterInputJSON(inputData, config.wantedKeys) # leaving only 'wanted' properies. See WantedKeys in Configuration.py
    queryString = rq.formSearchString(filteredInputData)

    connection = ConnectionManager()
    loginResult = connection.login(credentials) #login returns tuple(bool, str), therefore if login is succesful, the output is (True, tokenValue)
    
    if(not loginResult[0]):
        fm.writeJSON(loginResult[1], config.connErrorFile)
        exit()
    
    requestResult = connection.sendQuery(loginResult[1], queryString)
    fm.writeJSON(requestResult, config.outputFile)

    logoffResult = connection.logoff(loginResult[1])
    
    if(not logoffResult[0]):
        fm.writeJSON(loginResult[1], config.connErrorFile)
        exit()
    