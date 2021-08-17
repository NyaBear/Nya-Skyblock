import requests
import sys
import colorama
from colorama import Fore, Back, Style
import os

def introduction():
    print(Fore.MAGENTA + """
 ███▄    █▓██   ██▓ ▄▄▄           ██████  ██ ▄█▀▓██   ██▓ ▄▄▄▄    ██▓     ▒█████   ▄████▄   ██ ▄█▀
 ██ ▀█   █ ▒██  ██▒▒████▄       ▒██    ▒  ██▄█▒  ▒██  ██▒▓█████▄ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
▓██  ▀█ ██▒ ▒██ ██░▒██  ▀█▄     ░ ▓██▄   ▓███▄░   ▒██ ██░▒██▒ ▄██▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
▓██▒  ▐▌██▒ ░ ▐██▓░░██▄▄▄▄██      ▒   ██▒▓██ █▄   ░ ▐██▓░▒██░█▀  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
▒██░   ▓██░ ░ ██▒▓░ ▓█   ▓██▒   ▒██████▒▒▒██▒ █▄  ░ ██▒▓░░▓█  ▀█▓░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
░ ▒░   ▒ ▒   ██▒▒▒  ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒   ██▒▒▒ ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
░ ░░   ░ ▒░▓██ ░▒░   ▒   ▒▒ ░   ░ ░▒  ░ ░░ ░▒ ▒░ ▓██ ░▒░ ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
   ░   ░ ░ ▒ ▒ ░░    ░   ▒      ░  ░  ░  ░ ░░ ░  ▒ ▒ ░░   ░    ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░ 
         ░ ░ ░           ░  ░         ░  ░  ░    ░ ░      ░          ░  ░    ░ ░  ░ ░      ░  ░   
           ░ ░                                   ░ ░           ░                  ░               
""")
    print(Style.RESET_ALL)

introduction()

print(Fore.CYAN + "[ ! ] Hello, This tool lets you track your Hypixel Skyblock stats and profile.")
print(Style.RESET_ALL)

print(Fore.LIGHTYELLOW_EX + "Please enter your username: ")
username_input = input("[ > ] ")
os.system("clear")

def logic(ign):
    rr = requests.get("https://sky.shiiyu.moe/api/v2/coins/" + ign)
    r = rr.json()
    profiles = []
    if rr.status_code != 200:
        print("Something went wrong, perhaps your username is invalid or something regarding your network.")
        input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
        print(Style.RESET_ALL)
        sys.exit(0)
    for i in r["profiles"]:
        profiles.append(str(i))
    total_profiles = len(profiles)
    print(Fore.LIGHTYELLOW_EX + "Profiles - " + str(total_profiles))
    purse = 0
    for i in r["profiles"].keys():
        if "purse" in r["profiles"][i]:
            purse += round(r["profiles"][i]["purse"])
    bank = 0
    for i in r["profiles"].keys():
        if "bank" in r["profiles"][i]:
            bank += round(r["profiles"][i]["bank"])
    acc_value = bank + purse
    print("Total Gold - $" + str(acc_value))

introduction()
logic(username_input)
input(Fore.LIGHTYELLOW_EX + '[ > ] Press ENTER to exit: ')
print(Style.RESET_ALL)
