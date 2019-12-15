#!usr/bin/env python3

import collections
import json

class FileManager():
    def __init__(self):
        pass

    def readJSON(self, filename: str) -> dict():
        print("Reading json from " + filename)
        with open(filename, "r") as json_file:
            data = json.loads(json_file.read())

            return data

    def writeJSON(self, data: dict(), filename: str) -> None:
        print("Writing json into " + filename)
        with open(filename, "w") as json_file:
            json_file.write(json.dumps(data, indent=4, sort_keys=False))
        