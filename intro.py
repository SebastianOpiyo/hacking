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


# Exception Handling
# An example script to connect to Google using socket
# programming in Python
import socket  # for socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created"
except socket.error as err:
    print "socket creation failed with error:  %s" % (err)

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.geterror:

    # this means could not resolve the host
    print "there was an error resolving the host"
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print "the socket has successfully connected to google \
on port == %s" % (host_ip)


'''
# A server accepts both an ip address and a port as illustrated below.
# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print "socket binded to %s" % (port)

# put the socket into listening mode
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print 'Got connection from', addr

    # send a thank you message to the client.
    c.send('Thank you for connecting')

    # Close the connection with the client
    c.close()
