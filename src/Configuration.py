#!usr/bin/env python3

class Configuration():
    def __init__(self):
        # These config entries are default. Change them here or via CL arguments if needed
        self.wantedKeys = {"correspondent", "dateOpened", "rating", "category"}
        self.inputFile = "../InputFiles/test1.json"
        self.outputFile = "../OutputFiles/output0.json"
        self.connErrorFile = "../OutputFiles/connError.json"