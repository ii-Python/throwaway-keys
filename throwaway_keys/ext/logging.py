# Modules
from libs.colors import colored

# Simple loggers
def warn(m):

    print(colored(f"[warning]: {m}", "yellow"))
    print()
