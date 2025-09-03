import re
from scheme_token import Token, TokenType

# design notes:
# 1. I have duplicated work between the token regex match and deciding the token types.
#   - solution 1: do it like the example in the python docs for the "re" library (but it's pretty hairy?!)
#   - solution 2: scrap the regex matching and iterate by character. e.g. like in crafting interpreters. clean!
#   - for now I'll leave, though. this is just a toy parser.

class Scanner:
    """Scanner: scan tokens from raw Scheme source code.

    usage: `tokens = Scanner(source).getTokens()`
    """
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self._scan()

    def getTokens(self) -> list[Token]:
        return self.tokens

    SYMBOLS = {
        '(': TokenType.LEFT_PAREN,
        ')': TokenType.RIGHT_PAREN,
        '+': TokenType.PLUS,
        '-': TokenType.MINUS,
    }

    def _scan(self):
        # remove comments
        self.source = re.sub(r";;.*", '', self.source)
        # remove whitespace
        self.source = re.sub(r"(\n|\t|\r)", '', self.source)
        self.source = self.source.strip()

        regexes = [
                # number
                r"\s*(\d+)",
                # string literal
                r"\s*(\"[^\"]*\")",
                # symbols
                rf"\s*([{re.escape(''.join(self.SYMBOLS.keys()))}])",
                # keyword / identifier
                r"\s*([a-zA-Z_][a-zA-Z_0-9]*)", # todo: update. Scheme's names are flexbile, allowing e.g. '?'
        ]
        i = 0
        while True:
            match = None
            for regex in regexes:
                match = re.match(regex, self.source[i:])
                if match:
                    self._addToken(match.group(1))
                    i += match.end(0)
                    break

            if not match:
                break

        if i < len(self.source):
            # note: this simple regex approach doesn't let me report line nums.
            # solution: see design note #1
            raise RuntimeError("unexpected character: " + self.source[i])

    def _addToken(self, val: str):
        token = None
        if str.isdigit(val):
            token = Token(TokenType.NUMBER, val)
        elif val[0] == '"':
            token = Token(TokenType.STRING, val[1:-1])
        elif val in self.SYMBOLS:
            token = Token(self.SYMBOLS[val], val)
        elif str.isalnum(val):
            # todo: keyword checking goes here
            # todo: check actual Scheme name pattern, not just an alnum
            token = Token(TokenType.IDENTIFIER, val)
        else:
            raise SystemError("unreachable code - fell through token type check")

        self.tokens.append(token)
