#!/usr/bin/env python3
import sys
import requests
import urllib3
import colorama
import os
from fake_useragent import UserAgent

if os.name == "nt":
    colorama.init()
else:
    pass

if len(sys.argv) < 2:
    print("Использование: {} <username>".format(sys.argv[0]))
    exit(1)

ua = UserAgent()

# Disabling insecure request warnings for HTTPS sites
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SetColor:

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

print(SetColor.OKGREEN + r"""
 _   _               _____ _           _
| | | |___  ___ _ __|  ___(_)_ __   __| | ___ _ __
| | | / __|/ _ \ '__| |_  | | '_ \ / _` |/ _ \ '__|
| |_| \__ \  __/ |  |  _| | | | | | (_| |  __/ |
 \___/|___/\___|_|  |_|   |_|_| |_|\__,_|\___|_|
""" + "\n" + SetColor.ENDC + "by SmarklyaYT\n")


def check_username(user):
    not_found_msg = [
        "doesn&#8217;t&nbsp;exist",
        "doesn't exist",
        "no such user",
        "page not found",
        "could not be found",
        "https://pastebin.com/index",
        "user not found",
        "usererror-404",
        "he user id you entered was not found"
    ]

    headers = {
        'User-Agent':
        ua.random
        }

    print(SetColor.OKBLUE + "[*] Ищем..." + SetColor.ENDC)
    f = open(f'Отчёт_По_Запросу{sys.argv[1]}.txt', 'a+')
    with open("./sites.txt", "r") as sites:
        for site in sites:
            try:
                r = requests.get(site.format(sys.argv[1]).rstrip(), headers=headers, timeout=10)
                if r.status_code == 200:
                    found = [p in r.text.lower() for p in not_found_msg]
                    if True not in found:
                        print(SetColor.WARNING + "[+] Нашёл страничку: " + SetColor.ENDC + r.url)
                        f.write(f'{r.url}\n')
                    else:
                        print(SetColor.FAIL + "[-] Не нашёл страничку :( " + SetColor.ENDC)
            except requests.exceptions.RequestException as e:
                print(e)
                continue
    f.close()

if __name__ == "__main__":

    check_username(sys.argv[1])
