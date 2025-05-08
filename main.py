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
    done(input_text)

    input_text = """
    $$
    integer a, b;
    $$
    a = 10;
    b = 20;
    if (a != b) {
        print(a);
    }
    if (a <= b) {
        print(b);
    }
    $$
    """
    done(input_text)

    input_text = """
    $$
    integer x, y, z;
    $$
    x = 5;
    y = 10;
    z = 15;
    if (x < y && y <= z) {
        print(x);
        print(y);
        print(z);
    }
    if (z != x) {
        print(z);
    }
    $$
    """
    done(input_text)
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
