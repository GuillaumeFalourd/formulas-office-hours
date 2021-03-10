#!/usr/bin/python3
import os

from formula import formula

country = os.environ.get("RIT_COUNTRY")

formula.Run(country)
