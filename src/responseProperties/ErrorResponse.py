#!usr/bin/env python3

import json

class ErrorResponse(json.JSONEncoder):
    def __init__(self):
        self.errors = []