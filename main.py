from lexi import Lexical
from symboltable import SymbolTable
from syntax import Syntax
from assembly import Assembly

def done(input_text):
    table = SymbolTable()
    AC = Assembly() # For commands used

    # Create lexer and get tokens from program
    parser = Syntax(input_text, table, AC)
    output_content = parser.parse()
    
    table.printTable()
    AC.print_instructions()

def main():
    table = SymbolTable()
    AC = Assembly() # For commands used
    filenames = ["test1.txt"]

    for name in filenames:
        try:
            with open(name, "r") as file:
                input_text = file.read()

            parser = Syntax(input_text, table, AC)
            output_content = parser.parse()
            assem = AC.print_instructions()
            symbol = table.printTable()

            file_results = f"Analysis for {name}\n"
            file_results += "="*50 + "\n\n"
            file_results += "\n".join(output_content)
            file_results += "\n\n"

            file_results += assem
            file_results += "\n\n"

            file_results += symbol

            with open(f"{name}_output.txt", 'w') as output_file:
                output_file.write(file_results)

        except SyntaxError as e:
            print(f"Error parsing {name}: {e}")



if __name__ == "__main__":
    main()
