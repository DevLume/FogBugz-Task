#!usr/bin/env python3

from FileManager import FileManager
from RequestFormer import RequestFormer


if __name__ == "__main__":
    fm = FileManager()

    wantedKeys = {"userEmail", "dateOpened", "rating", "category"} # a set of properties used to filter the input JSON

    data = fm.readJSON("../InputFiles/test1.json")

    rf = RequestFormer()

    print(rf.filterInputJSON(data, wantedKeys)) # making sure that our Input JSON contains only needed properties 

    