#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool

def Run(age):
    print("Hello World!")
    print(f"{fg(2)}My age is {age}.{attr(0)}")
