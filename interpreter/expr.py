from abc import ABC, abstractmethod
from .scheme_token import Token
from .builtin import Builtin

class Expr(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def interpret(self):
        pass

class Atom(Expr):
    def __init__(self, token: Token):
        self.token = token

    def toString(self):
        return self.token.val

    def interpret(self):
        return self.token.val

class List(Expr):
    OPS = {
            '+'      : Builtin._plus,
            '-'      : Builtin._minus,
            # todo: add more
    }

    def __init__(self, elems: list[Expr]):
        self.elems = elems

    def toString(self):
        return '(' + ' '.join(map(lambda x: x.toString(), self.elems)) + ')'

    def interpret(self):
        evaled_elems = list(map(lambda x : x.interpret(), self.elems))

        op = evaled_elems[0]
        args = evaled_elems[1:]

        # func dispatch
        if op not in List.OPS:
            raise NotImplementedError(f'handling not implemented for operator {op}')
        return List.OPS[op](args)
