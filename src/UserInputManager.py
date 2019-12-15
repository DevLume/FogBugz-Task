#!usr/bin/env python3

from Credentials import Credentials
from Configuration import Configuration
from getpass import getpass
import base64
import sys 
import argparse


class UserInputManager():
    def __init__(self):
        pass 

    def getUserCredentials(self) -> Credentials:
        print("Hello, please introduce yourself")

        email = input("e-mail:")
        password = base64.b64encode(getpass("password:").encode())

        return Credentials(email, password)

    def parseCLArgs(self) -> Configuration:
        conf = Configuration()

        parser = argparse.ArgumentParser(description='Provide in/out files. WantedKeys filter is configured via source code change')
        parser.add_argument('-in', action="store", default="../InputFiles/test1.json", dest="inpt", help="Filename of the input file")
        parser.add_argument('-out', action="store", default="../OutputFiles/output0.json", dest="outpt", help="Filename of the output file")

        results = parser.parse_args()
        
        conf.inputFile = results.inpt
        conf.outputFile = results.outpt
        
        return conf