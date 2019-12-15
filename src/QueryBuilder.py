#!usr/bin/env python3

class QueryBuilder():
    def __init__(self):
        pass
    
    #Query is built by inheriting from needed property classes. Each base class has toString() method, 
    #which is called from the sub class when forming a query string
    def buildQuery(self, queryBases, queryJSON):
        class Query(*queryBases):
            def __init__(self, queryJSON, *base):
                self.body = "correspondent: "
                self.body += queryJSON['correspondent']
                for b in base:
                    self.body += " and "
                    b.__init__(self, queryJSON)
                    self.body += b.toString(self)
            
            def toString(self) -> str:
                return self.body
        
        return Query(queryJSON, *queryBases)

    