#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool


def Run(system, linux_os):
    print("Hello World!")
    print(f"{fg(2)}System: {system}.{attr(0)}")
    print(f"{fg(2)}Linux OS: {linux_os}.{attr(0)}")