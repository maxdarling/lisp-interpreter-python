import sys
from typing import TypeAlias
from scanner import Scanner
from scheme_token import Token, TokenType

'''
Exercise: implement a simple Scheme Lisp parser
usage: `python3 parser.py foo.scm`

we'll use a very basic AST representation of nested lists and string/number literals.
example: `(first (list 1 (+ 2 3) 9))` -> ["first", ["list", 1, ["+", 2, 3], 9]].

design notes/disclaimers:
- In the below grammar, I distinguished op from IDENTIFIER, but that causes ambiguity.
This would be fine in a Java grammar, say. But not in Scheme. Scheme is "lexically open" -
you can do stuff like `(define + *)`, so '+' is just an identifier, not a special symbol.
Interesting rabbit hole!
'''

# --- GRAMMAR (in progress) ---
# program    : expression*
# expression : list | atom
# list       : '(' expression* ')'
# atom       : op | IDENTIFIER | NUMBER | STRING
# op         : '+' | '-'

AstNode: TypeAlias = list #  todo: make into full class

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens + [Token(TokenType.EOF, None)]
        self.idx = 0

    # parse a single expression into an AstNode
    def parse(self) -> AstNode:
        return self._expression()

    def _expression(self) -> AstNode:
        if self._match(TokenType.LEFT_PAREN):
            return self._list()

        return self._atom().val # todo: change. currently sketch

    def _list(self) -> AstNode:
        node = []
        while not self._check(TokenType.RIGHT_PAREN):
            expr = self._expression()
            node.append(expr)

        self._consume(TokenType.RIGHT_PAREN, "Expected ')'.")
        return node


    def _atom(self) -> Token:
        if self._match(
            TokenType.PLUS, TokenType.MINUS,
            TokenType.IDENTIFIER,
            TokenType.NUMBER,
            TokenType.STRING
        ):
            return self._previous()

        raise RuntimeError("Expected expression.")

    def _peek(self) -> Token:
        return self.tokens[self.idx]

    def _previous(self) -> Token:
        return self.tokens[self.idx - 1]

    def _isAtEnd(self) -> bool:
        return self._peek().type == TokenType.EOF

    def _check(self, type: TokenType) -> bool:
        if self._isAtEnd():
            return False
        return type == self._peek().type

    def _advance(self):
        if self._isAtEnd():
            return
        self.idx += 1

    def _consume(self, type: TokenType, error_msg: str):
        if self._check(type):
            self._advance()
            return
        raise RuntimeError(error_msg)

    def _match(self, *types: TokenType) -> bool:
        for type in types:
            if self._check(type):
                self._advance()
                return True
        return False



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: parser.py [.scm file]")
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
