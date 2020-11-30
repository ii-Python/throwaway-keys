# Modules
from os import system
from shutil import which

# Install twine
if not which("twine"):
    system(f"{python} -m pip install --upgrade twine")

# Upload to PyPi
system(f"twine upload --repository pypi dist/*")

# Git commit
commit = input("Commit: ")
system(f"git add . && git commit -am \"{commit}\" && git push origin master")
