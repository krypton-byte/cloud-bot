"""
Author : Krypton Byte
Update : 28 Desember 2020
version: 0.0.1
"""
import requests, time, pyqrcode, re
from colorama.ansi import Fore
temp=0
loader=["|","/","-","\\"]
server=[
    "https://krypton-bot-server.herokuapp.com",
    "https://krypton-byte.herokuapp.com",
    "https://botpro-chappie.herokuapp.com",
    "https://krypton-chappie-bot.herokuapp.com"
]
def main():
    global temp
    print(Fore.LIGHTCYAN_EX+"-"+'-'*10+Fore.LIGHTRED_EX+"Krypton Bot"+Fore.LIGHTCYAN_EX+"-"+"-"*10)
    for i in range(len(server)):
        print(f"{Fore.LIGHTGREEN_EX}|\t{Fore.LIGHTBLUE_EX}{i} . {Fore.LIGHTGREEN_EX}Server {i}\t\t|")
    while True:
        try:
            uri=server[int(input(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}?{Fore.LIGHTYELLOW_EX}] {Fore.LIGHTMAGENTA_EX}Nomer Server : {Fore.LIGHTCYAN_EX}"))]
            break
        except IndexError:
            continue
        except KeyboardInterrupt:
            print(f"\r{Fore.LIGHTGREEN_EX}[-] Bye Bye      {Fore.RESET}")
            exit(1)
    req=requests.get(uri).text
    if "anda sudah login" in req.lower():
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTYELLOW_EX}] {Fore.LIGHTRED_EX}server sedang di gunakan{Fore.RESET}")
    else:
        while True:
            if "anda sudah login" in req.lower():
                print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}{loader[temp%len(loader)]}{Fore.LIGHTYELLOW_EX}] Tersambung", end="\r")
                req=requests.get(uri).text
                time.sleep(50)
                temp+=1
            elif re.search('<input type="hidden" name="qr" value="(.*?)">', req):
                print(pyqrcode.create(re.search('<input type="hidden" name="qr" value="(.*?)">', req)[1]).terminal(quiet_zone=1))
                req=requests.get(uri).text
                time.sleep(10)
            else:
                print(f"{Fore.LIGHTMAGENTA_EX}[-] Harap Hubungi Author{Fore.RESET}")
                break
main()