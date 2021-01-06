import os
import sys
from colorama.ansi import Fore
import socketio, pyqrcode, time
"""
 Author: Krypton Byte
 Update: Wed 6 Jan 2020 14:39
"""
angka=0
x=["-<>----","--<>---","---<>--","----<>-","-----<>","----<>-","---<>--","--<>---","-<>----","<>-----"]
server=[
    "http://bot-kbyte.herokuapp.com",
    "http://kbyte-bot.herokuapp.com",
    "http://krypton-application.herokuapp.com",
    "http://krypton-bot-indonesia.herokuapp.com",
    "http://my-xbot.herokuapp.com",
    "http://kits-api.herokuapp.com",
    "http://krypton-bot-server.herokuapp.com",
    "http://krypton-bot-server.herokuapp.com",
    "http://botpro-chappie.herokuapp.com",
    "http://krypton-chappie-bot.herokuapp.com",
    "http://krypton-byte.herokuapp.com"
]
if len(sys.argv)>1:
    if (val:=sys.argv[1]).isnumeric():
        if int(val) < len(server):
            pass
        else:
            print(f"{Fore.LIGHTRED_EX}Nomer Server Tidak Ada")
            exit()
    elif val == "list":
            print(f"""{Fore.LIGHTRED_EX}╭────「 {Fore.LIGHTGREEN_EX}BOT Server{Fore.LIGHTRED_EX} 」──────""")
            for i in enumerate(server):
                print(f"{Fore.LIGHTRED_EX}│ {Fore.LIGHTCYAN_EX}{i[0]}. {Fore.LIGHTYELLOW_EX}Server {i[0]}")
            print(f"{Fore.LIGHTRED_EX}╰────「 {Fore.LIGHTYELLOW_EX}Krypton Bot{Fore.LIGHTRED_EX}]」──────{Fore.LIGHTGREEN_EX}")
            exit()
    else:
            print(f"{Fore.LIGHTRED_EX}> {Fore.LIGHTGREEN_EX}python {Fore.LIGHTYELLOW_EX}{sys.argv[0]} {Fore.LIGHTGREEN_EX}[{Fore.LIGHTYELLOW_EX}<{Fore.LIGHTRED_EX}no_server{Fore.LIGHTYELLOW_EX}>{Fore.LIGHTGREEN_EX}|{Fore.LIGHTRED_EX}list{Fore.LIGHTGREEN_EX}]")
            exit()
else:
    print(f"{Fore.LIGHTRED_EX}> {Fore.LIGHTGREEN_EX}python {Fore.LIGHTYELLOW_EX}{sys.argv[0]} {Fore.LIGHTGREEN_EX}[{Fore.LIGHTYELLOW_EX}<{Fore.LIGHTRED_EX}no_server{Fore.LIGHTYELLOW_EX}>{Fore.LIGHTGREEN_EX}|{Fore.LIGHTRED_EX}list{Fore.LIGHTGREEN_EX}]")
    exit()
Sio=socketio.Client()
while True:
    try:
        Sio.connect(server[int(sys.argv[1])], namespaces=["/login","/serverx"])
        break
    except:
        continue
@Sio.on("qr", namespace="/login")
def recv_qr(data):
    print("\n\n"+pyqrcode.create(data.get("qr")).terminal(quiet_zone=1))
    time.sleep(10)
    Sio.emit("get_qr", namespace="/serverx")
@Sio.on("loged", namespace="/login")
def recv_log(data):
    global angka
    if data.get("Logged"):
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}[Krypton Bot]{Fore.LIGHTYELLOW_EX}] Tersambung [ "+x[angka%len(x)]+" ]", end="\r")
        angka+=1
        time.sleep(10)
        Sio.emit("get_qr", namespace="/serverx")
print("Connected Server: %s"%Sio.connected)
time.sleep(5)
Sio.emit("get_qr", namespace="/serverx")
Sio.wait()

    