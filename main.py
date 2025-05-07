from lexi import Lexical
from syntax import Syntax
from symboltable import SymbolTable 
from assembly import Assembly


def main():
    # Example input text - can be replaced with file reading if needed
    input_text = """
    integer x;
    x = 10;
    if (x > 5) {
        print(x);
    }
    """

    # Prepare symbol table 
    table = SymbolTable()

    # Create lexer and get tokens from program
    lexer = Lexical(input_text)
    tokens = lexer.parse()

    # Display tokens in a legible format
    print("Tokens:")
    print(f"{'Token Type':<15} Lexeme")
    print("-" * 30)
    for token_type, lexeme in tokens:
        print(f"{token_type:<15} {lexeme}")

    # Get only the identifiers 
    for token_type, lexeme in tokens:
        if token_type == "Identifier":
            table.insertAtTable(lexeme)

    print("\nParsing Output:")
    # Create syntax parser and parse input
    parser = Syntax(input_text)
    output_content = parser.parse()

    # Display parsing output legibly
    for line in output_content:
        print(line)

if __name__ == "__main__":
    main()
