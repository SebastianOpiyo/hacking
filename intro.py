'''
port = 21
banner = "FreeFloat FTP Server"

print("[+] Checking for " + banner + " on port " + str(port))
print(banner.upper())
print(banner.lower())
print(banner.replace('FreeFloat', 'Ability'))
print(banner.find('FTP'))


# LISTS

portList = []
portList.append(21)
portList.append(80)
portList.append(443)
portList.append(2)
portList.append(1000)

print(portList)
sot = sorted(portList)
print(sot)
pos = portList.index(80)

print("[+] There are " + str(pos) + " ports to scan before 80.")
portList.remove(21)
print(len(portList))

'''

import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.95.148", 21))
ans = s.recv(1024)
print(ans)

if ("FreeFloat Ftp Server (Version 1.0)" in ans):
    print("[+] FreeFloat FTP Server is vulnerable.")
elif ("3Com 3CDaemon FTP Server Version 2.0" in ans):
    print("[+] 3CDaemon FTP Server is vulnerable.")
elif ("Ability Server 2.34" in ans):
    print("[+] Ability FTP Server is vulnerable.")
elif ("Sami FTP Server 2.0.2" in ans):
    print("[+] Sami FTP Server is vulnerable.")
else:
    print("[-] FTP Server is not vulnerable.")
