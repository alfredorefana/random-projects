"""
This simple python script identifying your os by using platform library
Read more: https://docs.python.org/3.8/library/platform.html
"""

import platform

# Everything in one line, well basically the "uname" on *nix 
print(platform.uname())

# Separately handled
print("Node / Hostname:", platform.node())
print("Platform:", platform.system())
print("Architecture:", platform.architecture())
print("Version:", platform.version())
print("Release:", platform.release())
print("Machine:", platform.machine())
print("Processor:", platform.processor())

# TO be used for specific case
try:
    my_platform = platform.system()
    if my_platform == "Linux":
        print("You are running a Linux machine.")
        # Execute steps for Linux machines here.
    elif my_platform == "Windows":
        print("You are running a Windows machine.")
        # Execute steps for WIndows machines here.
    elif my_platform == "Darwin":
        print("You are running a MacOS machine.")
        # Execute steps for MacOS machines here.
except AttributeError:
    print("Unidentified system.")