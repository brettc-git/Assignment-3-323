import sys
from lexi import Lexical
from symboltable import SymbolTable

class Assembly:
    def __init__(self):
        self.stack = []
        self.memory_register = {}
        self.instructions = []

    def print_instructions(self):
        output = "ASSEMBLY INSTRUCTIONS USED\n"
        for index, line in enumerate(self.instructions, start = 1):
            output += f"{index}: {line}\n"
        return output

    def add_neq(self, operand1, operand2):
        self.add_instruction("NEQ", operand1, operand2)

    def add_leq(self, operand1, operand2):
        self.add_instruction("LEQ", operand1, operand2)

    def add_geq(self, operand1, operand2):
        self.add_instruction("GEQ", operand1, operand2)


    def execute_instruction(self, command, value = None):
        if command == "PUSHI": # Push integer value onto top of stack
            self.stack.append(value)
            self.instructions.append(f"PUSHI {value}")
        elif command == "PUSHM": # Push value stored at memory location onto TOS
            loaded_val = self.memory_register.get(value, 0)
            self.stack.append(loaded_val)
            self.instructions.append(f"PUSHM {value}")
        elif command == "POPM": # Pop value from TOS and store at ML
            if not self.stack:
                print("Error: Stack empty on POPM")
                return
            popped_val = self.stack.pop()
            self.memory_register[value] = popped_val
            self.instructions.append(f"POPM {value}")
        elif command == "SOUT": # Pop vlaue from tOS and output to standard output
            value = self.stack.pop()
            print(f"Output: {value}")
            self.instructions.append("SOUT")
        elif command == "SIN":
            self.stack.append(value)
            self.instructions.append("SIN")
        elif command == "A":
            if len(self.stack) < 2:
                print("Error: Not enough values on stack for A")
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a+b)
            self.instructions.append("A")
        elif command == "S":
            if len(self.stack) < 2:
                print("Error: Not enough values on stack for S")
                return
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a-b)
            self.instructions.append("S")
        elif command == "M":
            if len(self.stack) < 2:
                print("Error: Not enough values on stack for M")
                return
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a*b)
            self.instructions.append("M")
        elif command == "D":
            if len(self.stack) < 2:
                print("Error: Not enough values on stack for D")
                return
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a/b)
            self.instructions.append("D")
        elif command == "GRT": # Pop two items from stack and push 1 onto TOS if second item is greater, otherwise push 0
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(1 if a>b else 0)
            self.instructions.append("GRT")
        elif command == "LES":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(1 if a<b else 0)
            self.instructions.append("LES")
        elif command == "EQU":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(1 if a==b else 0)
            self.instructions.append("EQU")
        elif command == "NEQ":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(1 if a!=b else 0)
            self.instructions.append("NEQ")
        elif command == "GEQ":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(1 if a>=b else 0)
            self.instructions.append("GEQ")
        elif command == "LEQ":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(1 if a<=b else 0)
            self.instructions.append("LEQ")
        elif command == "JMP0": # Pop stack and if value is 0 then jmp to Instruction Location (IL)
            self.stack.pop()
            self.instructions.append(f"JMP0 {value}")
        elif command == "JMP": # Unconditionally jump to IL
            self.instructions.append(f"JMP {value}")
        elif command == "LABEL":
            self.instructions.append("LABEL")
        else:
            print("Invalid command")
