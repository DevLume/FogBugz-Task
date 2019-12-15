#!usr/bin/env python3

class category():
    def __init__(self, queryJSON):
        self.category = queryJSON['category']

    def toString(self) -> str:
        return "category: " + self.category
