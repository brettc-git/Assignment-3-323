import sys
from lexi import Lexical
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


    def execute_instruction(self, instr, value = None):
        command = ""
        if command == "PUSHI": # Push integer value onto top of stack
            self.stack.append(value)
            self.instructions.append(f"PUSHI {value}")
        elif command == "PUSHM": # Push value stored at memory location onto TOS
            loaded_val = self.memory_register.get(value, 0)
            self.stack.append(loaded_val)
            self.instructions.append(f"PUSHM {value}")
        elif command == "POPM": # Pop value from TOS and store at ML
            popped_val = self.stack.pop()
            self.memory_register[value] = popped_val
            self.instructions.append(f"POPM {value}")
        elif command == "SOUT": # Pop vlaue from tOS and output to standard output
            value = self.stack.pop()
            print(f"Output: {value}")
            self.instructions.append("SOUT")
        elif command == "SIN":
            self.stack.append(value)
        elif command == "A":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a+b)
            self.instructions.append("A")
        elif command == "S":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a-b)
            self.instructions.append("S")
        elif command == "M":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a*b)
            self.instructions.append("M")
        elif command == "D":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a/b)
            self.instructions.append("D")
        elif command == "GRT": # Pop two items from stack and push 1 onto TOS if second item is greater, otherwise push 0
            self.instructions.append("GRT")
        elif command == "LES":
            self.instructions.append("LES")
        elif command == "EQU":
            self.instructions.append("EQU")
        elif command == "NEQ":
            self.instructions.append("NEQ")
        elif command == "GEQ":
            self.instructions.append("GEQ")
        elif command == "LEQ":
            self.instructions.append("LEQ")
        elif command == "JMP0": # Pop stack and if value is 0 then jmp to Instruction Location (IL)
            pass
        elif command == "JMP": # Unconditionally jump to IL
            pass
        elif command == "LABEL":
            pass # Simply pass, no action required
        else:
            print("Invalid command")