#!/usr/bin/python3
import os

from formula import formula

name = os.environ.get("RIT_NAME")

formula.Run(name)
