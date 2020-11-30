# Modules
import sys

# Functions that handle arguments
def uses():

    for arg in sys.argv:
        if arg.startswith("--use-"):
            return arg[6:]

    return None

def get_rounds():

    for arg in sys.argv:

        if arg.startswith("--rounds="):

            rounds = arg.split("=", 1)[1]

            try: return int(rounds)
            except: raise InvalidRounds("'{}' was not recognized as a valid integer.".format(rounds))

    return 3

def get_length():

    for arg in sys.argv:

        if arg.startswith("--length="):

            length = arg.split("=", 1)[1]

            try: return int(length)
            except: raise InvalidLength("'{}' was not recognized as a valid integer.".format(rounds))

    return 75
