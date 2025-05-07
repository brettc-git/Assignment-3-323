import sys
from lexi import Lexical
from syntax import Syntax
from symboltable import SymbolTable

class Assembly:
    def __init__(self):
        self.stack = []
        self.memory_register = {}
        self.instructions = []

    def print_instructions(self):
        print("ASSEMBLY INSTRUCTIONS USED")
        for line in self.instructions:
            print(line)


    def execute_instruction(self, instr):
        command = ""
        if command == "PUSHI": # Push integer value onto top of stack
            self.stack.append(value)
            self.instructions.append("PUSHI " + str(value))
        elif command == "PUSHM": # Push value stored at memory location onto TOS
            pass
        elif command == "POPM": # Pop value from TOS and store at ML
            pass
        elif command == "SOUT": # Pop vlaue from tOS and output to standard output
            value = self.stack.pop()
            print(f"Output: {value}")
            self.instructions.append("SOUT")
        elif command == "SIN":
            pass
        elif command == "A":
            self.instructions.append("A")
        elif command == "S":
            self.instructions.append("S")
        elif command == "M":
            self.instructions.append("M")
        elif command == "D":
            self.instructions.append("D")
        elif command == "GRT": # Pop two items from stack and push 1 onto TOS if second item is greater, otherwise push 0
            self.instructions.append("GRT")
        elif command == "LES":
            self.instructions.append("LES")
        elif command == "EQU":
            pass
        elif command == "NEQ":
            pass
        elif command == "GEQ":
            pass
        elif command == "LEQ":
            pass
        elif command == "JMP0": # Pop stack and if value is 0 then jmp to Instruction Location (IL)
            pass
        elif command == "JMP": # Unconditionally jump to IL
            pass
        elif command == "LABEL":
            pass # Simply pass, no action required
        else:
            print("Invalid command")