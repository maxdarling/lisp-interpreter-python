from enum import Enum

class TokenType(Enum):
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    NUMBER = 3
    STRING = 4
    IDENTIFIER = 5
    # built-in operators
    PLUS = 6
    MINUS = 7
    EOF = 8

class Token:
    def __init__(self, type: TokenType, val: str):
        self.type = type
        self.val = val

    def __str__(self):
        return f'Token("{self.val}" : {self.type.name})'

    def __repr__(self):
        return self.__str__()