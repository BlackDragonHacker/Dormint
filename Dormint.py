import os
import sys
import json
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green= Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
black = Fore.LIGHTBLACK_EX
reset = Style.RESET_ALL


class Dormint:
    def __init__(self):
        self.base_headers = {
            "host": "api.dormint.io",
            "connection": "keep-alive",
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 4A / 5A Build/QQ3A.200805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36",
            "content-type": "application/json",
            "origin": "https://web.dormint.io",
            "x-requested-with": "tw.nekomimi.nekogram",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://web.dormint.io/",
            "accept-language": "en,en-US;q=0.9",
        }
        

    def load_data(self):
        datas = open("data.txt", "r").read().splitlines()
        self.log(f"\033[1;93mTotal account's: {white}{len(datas)}{reset}") 
        self.log("\033[1;93m--------------------------------\033[0m") 
        if len(datas) <= 0:
            self.log(f"input you token account in data.txt first !")
            sys.exit()

        return datas

    def start_farming(self, token):
        url = "https://api.dormint.io/tg/farming/start"
        headers = self.base_headers.copy()
        data = json.dumps({"auth_token": token})
        res = self.http(url, headers, data)
        if "ok" in res.text.lower():
            self.log(f"\033[1;92mStart farming successfully !{reset}")
            return True

        self.log(f"{red}Start farming failure !")
        return False

    def claim_farming(self, token):
        url = "https://api.dormint.io/tg/farming/claimed"
        data = json.dumps({"auth_token": token})
        headers = self.base_headers.copy()
        res = self.http(url, headers, data)
        if "ok" in res.text.lower():
            self.log("\033[1;92mClaim farming successfully !\033[0m")
            return True

        self.log(f"{red}Claim farming failure !")
        return False

    def status_farming(self, token):
        url = "https://api.dormint.io/tg/farming/status"
        headers = self.base_headers.copy()
        data = json.dumps({"auth_token": token})
        while True:
            res = self.http(url, headers, data)
            farming_status = res.json()["farming_status"]
            farming_left = res.json()["farming_left"]
            if farming_status == "farming_status_not_started":
                self.log("\033[1;93mFarming not started !\033[0m")
                result = self.start_farming(token)
                continue

            if farming_status == "farming_status_started":
                self.log("\033[1;93mFarming is started !\033[0m")
                farming_amount = res.json()["farming_value"]
                self.log("\033[1;92mFarming balance : \033[1;97m{}\033[0m".format(farming_amount))
                self.log("\033[1;96mNext claim in : \033[1;97m{}\033[0m".format(self.secto(round(farming_left))))
                self.log("\033[1;93m--------------------------------\033[0m")
                return round(farming_left) + 5

            if farming_status == "farming_status_finished":
                self.log("\033[1;96mFarming is finished !\033[0m")
                result = self.claim_farming(token)
                continue

    def user_info(self, token):
        url = "https://api.dormint.io/user/info"
        headers = self.base_headers.copy()
        data = json.dumps({"auth_token": token})
        res = self.http(url, headers, data)
        if '"ok"' not in res.text.lower():
            self.log(f"{red}something wrong !, check http log for more information !")
            return False

        balance = res.json()["sleepcoin_balance"]
        self.log("\033[1;92mBalance : \033[1;97m{}\033[0m".format(balance))

    def main(self):
        banner = "\033[1;91m" + r"""  
  ___    _                  _     
 (  _`\ (_ )               ( )    
 | (_) ) | |    _ _    ___ | |/') 
 |  _ <' | |  /'_` ) /'___)| , <  
 | (_) ) | | ( (_| |( (___ | |\`\ 
 (____/'(___)`\__,_)`\____)(_) (_)
""" + "\033[0m" + "\033[1;92m" + r"""  
  ___                                     
 (  _`\                                   
 | | ) | _ __    _ _    __     _     ___  
 | | | )( '__) /'_` ) /'_ `\ /'_`\ /' _ `\
 | |_) || |   ( (_| |( (_) |( (_) )| ( ) |
 (____/'(_)   `\__,_)`\____)(_) (_) (_) (_)
                     ( )_) |              
                      \___/'              
""" + "\033[0m" + "\033[1;93m" + r"""  
  _   _                _                  
 ( ) ( )              ( )                 
 | |_| |   _ _    ___ | |/')    __   _ __ 
 |  _  | /'_` ) /'___)| , <   /'__`\( '__)
 | | | |( (_| |( (___ | |\`\ (  ___/| |   
 (_) (_)`\__,_)`\____)(_) (_)`\____)(_)   
""" + "\033[0m"
        banner2 = "\033[1;96m----------------------------------\033[0m"
        banner3 = "\033[1;93mScript created by: Black Dragon Hacker\033[0m"
        banner4 = "\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m"
        banner5 = "\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m"
        banner6 = "\033[1;96m----------------------------------\033[0m"
        banner7 = "\033[1;38;2;139;69;19;48;2;173;216;230m--------[Dormint Bot]--------\033[0m"
        banner8 = "\033[1;96m----------------------------------\033[0m"
        arg = sys.argv
        if "marinkitagawa" not in arg:
            os.system("cls" if os.name == "nt" else "clear")
        print(banner)
        print(banner2)
        print(banner3)
        print(banner4)
        print(banner5)
        print(banner6)
        print(banner7)
        print(banner8)
        
        accounts = self.load_data()
      
        while True:
            list_countdown = []
            _start = int(time.time())
            for no,account in enumerate(accounts):
                self.log("\033[1;91mAccount no: \033[1;97m{}\033[0m".format(no + 1))
                self.user_info(account)
                result = self.status_farming(account)
                list_countdown.append(result)
                

            _end = int(time.time())
            _tot = _end - _start
            _min = min(list_countdown) - _tot
            if _min <= 0:
                continue

            self.countdown(_min)
    
    def secto(self,t):
            minute, second = divmod(t, 60)
            hour, minute = divmod(minute, 60)
            hour = str(hour).zfill(2)
            minute = str(minute).zfill(2)
            second = str(second).zfill(2)
            return f"{hour}:{minute}:{second}"

    def countdown(self, t):
        while t:
            minute, second = divmod(t, 60)
            hour, minute = divmod(minute, 60)
            hour = str(hour).zfill(2)
            minute = str(minute).zfill(2)
            second = str(second).zfill(2)
            
            
            print(f"waiting until {hour}:{minute}:{second} ", flush=True, end="\r")
            t -= 1
            time.sleep(1)
        print("                          ", flush=True, end="\r")

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{black}{reset}{msg}")

    def http(self, url, headers, data=None):
        while True:
            try:
                if data is None:
                    res = requests.get(url, headers=headers)
                    open("http.log", "a", encoding="utf-8").write(f"{res.text}\n")
                    if "<html>" in res.text:
                        self.log("failed get json response !")
                        time.sleep(2)
                        continue

                    return res

                if data == "":
                    res = requests.post(url, headers=headers)
                    open("http.log", "a", encoding="utf-8").write(f"{res.text}\n")
                    if "<html>" in res.text:
                        self.log(f"failed get json response !")
                        time.sleep(2)
                        continue

                    return res

                res = requests.post(url, headers=headers, data=data)
                open("http.log", "a", encoding="utf-8").write(f"{res.text}\n")
                if "<html>" in res.text:
                    self.log(f"failed get json response !")
                    time.sleep(2)
                    continue

                return res

            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                self.log("connection timeout / connection error !")
                continue


if __name__ == "__main__":
    try:
        app = Dormint()
        app.main()
    except KeyboardInterrupt:
        sys.exit()
