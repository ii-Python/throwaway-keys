# Colors
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "cyan": "\033[36m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "reset": "\033[0m"
}

# Function for printing colored text
def colored(text, color):
    return colors[color] + text + colors["reset"]
    