#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool

def Run(days):
    print("Hello World!")
    print(f"{fg(2)}Days: {days}.{attr(0)}")

    items = days.split("|")
    print("Items:", items)
    
    loop = 0
    for item in items:
        loop = loop +1
        print(f"Day {loop}:", item)
