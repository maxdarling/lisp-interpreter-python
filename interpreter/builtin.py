# design note:
# - I'm uncertain on this design. I'd have stuffed it at the bottom of Expr if not for
# the lack of hoisting in python.

class Builtin:
    def _plus(args):
        if len(args) == 0:
            raise RuntimeError("expected arguments for +")
        args = list(map(lambda x: int(x), args))
        return sum(args)

    def _minus(args):
        if len(args) == 0:
            raise RuntimeError("expected arguments for -")
        args = list(map(lambda x: int(x), args))
        if len(args) == 1:
            return -args[0]
        return args[0] - sum(args[1:])
