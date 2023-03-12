import os
import urllib.request
# import urllib2
import pathlib

file = "passwords.txt"
url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt"

# path = os.path.abspath(file)
# urlpath = os.path.abspath(url)
file = url

try:
    f = urllib.request.urlopen(file)
    print(f"urllib: {file} is open")
except:
    print(f"urllib cannot open {file}")
    try:
        f = open(file)
        print(f"open: {file} is open")
    except:
        print(f"cannot open {file}")
        exit()

for line in f:
    print(line.decode('utf-8').strip())