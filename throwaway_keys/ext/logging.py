# Modules
from throwaway_keys.libs.colors import colored

# Simple loggers
def warn(m):

    print(colored(f"[warning]: {m}", "yellow"))
    print()
