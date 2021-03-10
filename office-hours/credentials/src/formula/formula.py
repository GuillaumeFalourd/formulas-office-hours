#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool

def Run(username):
    print("Hello World!")
    print(f"{fg(2)}Github Username: {username}.{attr(0)}")
