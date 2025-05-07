from lexi import Lexical
from syntax import Syntax

def main():
    # Example input text - can be replaced with file reading if needed
    input_text = """
    integer x;
    x = 10;
    if (x > 5) {
        print(x);
    }
    """

    # Create lexer and get tokens
    lexer = Lexical(input_text)
    tokens = lexer.parse()

    # Limit tokens to first 10 for brevity
    limited_tokens = tokens[:10]

    # Display tokens in a legible format
    print("Tokens (limited to first 10):")
    print(f"{'Token Type':<15} Lexeme")
    print("-" * 30)
    for token_type, lexeme in limited_tokens:
        print(f"{token_type:<15} {lexeme}")

    print("\nParsing Output:")
    # Create syntax parser and parse input
    parser = Syntax(input_text)
    output_content = parser.parse()

    # Display parsing output legibly
    for line in output_content:
        print(line)

if __name__ == "__main__":
    main()
