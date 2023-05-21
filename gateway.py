#! /usr/bin/env python3
from colorama import Fore
import os
import sys


database = {
    "admin": "0000"
    }

def check_usr_pass(user, password):
    if database.get(user, 'none') == password:
        print(f"{Fore.GREEN}Logging in was sucessful{Fore.RESET}")
        print("Welcome ", user)
        sys.exit(0)
    else:
        print(f"{Fore.RED}An error occuerd!")
        sys.exit(-1)
        
username = input("Enter your user name: ")
password = input("Enter you password: ")

if __name__ == "__main__":
    check_usr_pass(username, password)
