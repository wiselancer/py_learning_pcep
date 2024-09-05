class NonIntArgumentException(Exception):
    def __init__(self, arg):
        super().__init__(f"Argument {arg} is not an integer")


def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise NonIntArgumentException(arg)
        return func(*args)

    return wrapper
