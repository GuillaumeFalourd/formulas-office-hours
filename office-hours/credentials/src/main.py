#!/usr/bin/python3
import os

from formula import formula

username = os.environ.get("RIT_GITHUB_USERNAME")

formula.Run(username)
