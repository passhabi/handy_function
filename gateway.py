#! /usr/bin/env python3
from colorama import Fore
import os
import sys


username = input("Enter your user name:")

print("Welcome ", username)
print(Fore.RED, "An error occuerd!") # data should be checked with datebase.

sys.exit(-1)