import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Fil32")._site_view_()
elif 'aarch' in arc:
	__import__("Fil")._site_view_()
else:
	exit(f' Unknow device machine {arc}')
import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Enjoy Kro ❤ \033[1;37m")
    os.system('xdg-open https://facebook.com/groups/1017905562448002/');time.sleep(1)
    from FUCK import Fuck_U
    Fuck_U()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
