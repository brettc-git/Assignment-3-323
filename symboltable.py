import sys
from lexi import Lexical

class SymbolTable:


    def __init__(self):
# Our initial memory address, gets incremented by 1 every time a new identifier is added
        self.memory_address = 10000
        self.table = {}


    # Insert identifier into table
    def insertAtTable(self, identifier):
        if identifier in self.table:
            raise Exception("Identifier already exists in symbol table/Already declared.")
        self.table[identifier] = {
            "address": self.memory_address, # include also type of lexeme like integer
        }

        self.memory_address += 1 # i.e. if memory address is 10000, next one will be 10001

    # Check if identifier already exists (boolean)
    def checkTable(self, identifier):
        if identifier not in self.table:
            raise Exception(f"Error: Variable '{identifier}' not declared")
        return self.table[identifier]

    def printTable(self):
        for key, value in self.table.items():
            print(key, value)

