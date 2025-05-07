import sys
from lexi import Lexical
from syntax import Syntax

class SymbolTable:


    def __init__(self):

# Our initial memory address, gets incremented by 1 every time a new identifier is added
        Memory_Address = 10000
        self.table = {}

    # Check if identifier already exists (boolean)
    def checkTable(self, identifier):
        if len(self.table) == 0:
            return False

    def insertAtTable(self, identifier):
        if identifier in self.table:
            print("Error: identifier already exists in the symbol table")
        else:
            self.table[identifier] = {}
            Memory_Address = Memory_Address + 1


    def printTable(self):
        for key, value in self.table.items():
            print(key, value)

