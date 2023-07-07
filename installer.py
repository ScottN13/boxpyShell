import subprocess
import sys
from timeit import default_timer as timer

# Runs pip in a subprocess, basically running a command inside python.
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("# Installing/checking modules")

# Add any python module you want here.
modules = ["rich","python-git"]


start = timer() # Obtains time from start of the program

for i in modules:
    install(i)

elapsed = timer() # Obtains time from end of the program
print(f"# Success! Done in",elapsed - start)

subprocess.run(["python3", "updater.py"]) # Run updater.py. Honestly this can make for a better script parser

    