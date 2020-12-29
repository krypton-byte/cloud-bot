"""
Author : Krypton Byte
Update : 28 Desember 2020
version: 0.0.1
"""
from os import getcwd
import requests, time, pyqrcode, re, os, json
from colorama.ansi import Fore
temp=0
loader=["|","/","-","\\"]
server=[
    "https://krypton-bot-server.herokuapp.com",
    "https://krypton-byte.herokuapp.com",
    "https://botpro-chappie.herokuapp.com",
    "https://krypton-chappie-bot.herokuapp.com"
]
def main2():
    print(f"""{Fore.LIGHTRED_EX}╭────「 {Fore.LIGHTGREEN_EX}BOT Menu{Fore.LIGHTRED_EX} 」──────
{Fore.LIGHTRED_EX}│ {Fore.LIGHTCYAN_EX}1. {Fore.LIGHTYELLOW_EX}Set Nama & Author
{Fore.LIGHTRED_EX}│ {Fore.LIGHTCYAN_EX}2. {Fore.LIGHTYELLOW_EX}Run Bot
{Fore.LIGHTRED_EX}│ {Fore.LIGHTCYAN_EX}3. {Fore.LIGHTYELLOW_EX}Exit
{Fore.LIGHTRED_EX}╰────────────────────────""")
    while True:
        pilihan=input(f"""{Fore.LIGHTRED_EX}╭────「 {Fore.LIGHTGREEN_EX}Input Menu{Fore.LIGHTRED_EX} 」────
{Fore.LIGHTRED_EX}│
{Fore.LIGHTRED_EX}╰─>{Fore.LIGHTGREEN_EX} """)
        if pilihan in ["1", "01"]:
            setup()
        elif pilihan in ["2", "02"]:
            main()
            break
        elif pilihan in ["3", "03"]:
            break
def setup():
    while True:
        print(f"""{Fore.LIGHTRED_EX}╭────「 {Fore.LIGHTGREEN_EX}Input Menu{Fore.LIGHTRED_EX} 」────
{Fore.LIGHTRED_EX}│""")
        botname=input(f"{Fore.LIGHTRED_EX}╰─[{Fore.LIGHTYELLOW_EX}Nama Bot{Fore.LIGHTRED_EX}]> {Fore.LIGHTGREEN_EX}")
        author =input(f"{Fore.LIGHTRED_EX}╰─[{Fore.LIGHTYELLOW_EX}Author Bot]{Fore.LIGHTRED_EX}> {Fore.LIGHTGREEN_EX}")
        if botname and author:
            open("data.json","w").write(json.dumps({
                    "botname":botname,
                    "author":author
            }, indent=4))
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTYELLOW_EX}] {Fore.LIGHTRED_EX}Set Nama dan author berhasil{Fore.RESET}")
            main2()
def main():
    global temp
    loadjs=json.loads(open("data.json","r").read()) if "data.json" in os.listdir(os.getcwd()) else {"botname":"Krypton-Bot","author":"6283172366463"}
    print(f"""{Fore.LIGHTRED_EX}╭────「 {Fore.LIGHTGREEN_EX}BOT Server{Fore.LIGHTRED_EX} 」──────""")
    for i in range(len(server)):
        print(f"{Fore.LIGHTRED_EX}│ {Fore.LIGHTCYAN_EX}{i}. {Fore.LIGHTYELLOW_EX}Server {i}")
    print(f"{Fore.LIGHTRED_EX}╰──────────────────────────")
    while True:
        try:
            print(f"""{Fore.LIGHTRED_EX}╭────「 {Fore.LIGHTGREEN_EX}Input Menu{Fore.LIGHTRED_EX} 」──────
{Fore.LIGHTRED_EX}│""")
            uri=server[int(input(f"{Fore.LIGHTRED_EX}╰─[{Fore.LIGHTYELLOW_EX}Nomer Server{Fore.LIGHTRED_EX}]> {Fore.LIGHTGREEN_EX}"))]
            break
        except IndexError:
            continue
        except KeyboardInterrupt:
            print(f"\r{Fore.LIGHTGREEN_EX}[-] Bye Bye      {Fore.RESET}")
            exit(1)
    req=requests.get(uri, params={"botname":loadjs.get("botname","Krypton Bot"),"author":loadjs.get("author","6283172366463")}).text.lower()
    if "anda sudah login" in req.lower():
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTYELLOW_EX}] {Fore.LIGHTRED_EX}server sedang di gunakan{Fore.RESET}")
    else:
        while True:
            if "anda sudah login" in req:
                print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}{loader[temp%len(loader)]}{Fore.LIGHTYELLOW_EX}] Tersambung", end="\r")
                req=requests.get(uri, params={"botname":loadjs.get("botname","Krypton Bot"),"author":loadjs.get("author","6283172366463")}).text.lower()
                time.sleep(50)
                temp+=1
            elif re.search('<input type="hidden" name="qr" value="(.*?)">', req):
                print(pyqrcode.create(re.search('<input type="hidden" name="qr" value="(.*?)">', req)[1]).terminal(quiet_zone=1))
                req=requests.get(uri).text
                time.sleep(10)
            else:
                print(f"{Fore.LIGHTMAGENTA_EX}[-] Harap Hubungi Author{Fore.RESET}")
                break
main2()