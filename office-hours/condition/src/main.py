#!/usr/bin/python3
import os

from formula import formula

system = os.environ.get("RIT_SYSTEM")
linux_os = os.environ.get("RIT_LINUX_OS")

formula.Run(system, linux_os)
