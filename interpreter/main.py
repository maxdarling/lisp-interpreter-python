import sys
from .scanner import Scanner
from .parser import Parser

# Exercise: implement a simple Scheme Lisp parser
#
# extension: implement basic interpretation
#
# used for recurse center interview on 9/9/25. in ~25 mins I implemented addition.
# this code is now a couple hours of heavy cleanup beyond that.
#
# thoughts:
# - i want static types
# - i want a data-only Expr class, with the interpreting logic hooked up via
# the interpreter pattern, a la crafting iterpreters.
#
# todo:
# - implement define for vars
# - implement functions
# - implement more builtin ops

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
        ast = Parser(tokens).parse()
        print(ast.toString())
        print("\nVALS:")
        print(ast.interpret())
