import sys
from .scanner import Scanner
from .parser import Parser

# Exercise: implement a simple Scheme Lisp parser
#
# we'll use a very basic AST representation of nested lists and string/number literals.
# example: `(first (list 1 (+ 2 3) 9))` -> ["first", ["list", 1, ["+", 2, 3], 9]].
#
# extension: implement basic interpretation

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 -m interpreter.main [.scm file]")
        exit(0)

    filepath = sys.argv[1]
    with open(filepath, 'r', encoding=None) as f:
        raw = f.read()
        print("RAW:")
        print(raw)
        print("\nTOKENS:")
        tokens = Scanner(raw).getTokens()
        print(tokens)
        print("\nAST:")
        print(Parser(tokens).parse())
