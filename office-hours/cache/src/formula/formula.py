#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool


def Run(name):
    print("Hello World!")
    print(f"{fg(2)}My name is {name}.{attr(0)}")
