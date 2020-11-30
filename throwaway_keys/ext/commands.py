# Modules
import sys
from libs.colors import colored
from ext.defaults import generators

# Locate all arguments
def load_args():

    args = []
    big_args = []
    for arg in sys.argv:
        if arg.startswith("-") and not arg.startswith("--"):
            args.append(arg[1:])
        elif arg.startswith("--"):
            big_args.append(arg[2:])

    return (args, big_args)

# Run commands
def run_commands():

    args, long_args = load_args()

    if "h" in args or "help" in long_args:

        print("The", colored("Throwaway Key", "yellow"), "Project")
        print("=========================")

        print()
        print("usage: python3 -m throwaway_keys [options]")
        print("available hashing algorithms:")

        print(" ", "".join(_ + ", " for _ in generators)[:-2])

        print()
        print("to use a custom generator: --use-<generator_name>")
        print("to setup custom rounds: --rounds=<integer>")
        print("to setup custom length: --length=<integer> (only applicable with some generators)")

        exit()
