# Modules
from os import system
from shutil import which

# Locate python
python = "python"
if which("python3"):
    python = "python3"

# Run build
system(f"{python} setup.py sdist bdist_wheel")
