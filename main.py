from lexi import Lexical
from symboltable import SymbolTable
from syntax import Syntax
from assembly import Assembly


def main():
    # Example input text - can be replaced with file reading if needed
    input_text = """
    $$
    integer x;
    $$
    x = 10;
    if (x > 5) {
        print(x);
    }
    $$
    """

    # Prepare symbol table 
    table = SymbolTable()
    AC = Assembly() # For commands used

    # Create lexer and get tokens from program
    parser = Syntax(input_text, table, AC)
    output_content = parser.parse()
    
    table.printTable()
    AC.print_instructions()
    # lexer = Lexical(input_text)
    # tokens = lexer.parse()

    # # Display tokens in a legible format
    # print("Tokens:")
    # print(f"{'Token Type':<15} Lexeme")
    # print("-" * 30)
    # for token_type, lexeme in tokens:
    #     print(f"{token_type:<15} {lexeme}")

   
    # print("\nParsing Output:")
    # # Create syntax parser and parse input
    # parser = Syntax(input_text)
    # output_content = parser.parse()

    # # Display parsing output legibly
    # for line in output_content:
    #     print(line)



if __name__ == "__main__":
    main()
