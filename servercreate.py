#!/usr/bin/env python3
# Echo server program

import socket

host = socket.gethostname()
print(host)
port = 12345

# calling the functions socket, and sub-functions bind, listen
s = socket.socket()
s.bind((host, port))
s.listen(5)

conn, addr = s.accept()

print('Got connection from ', addr[0], '(', addr[1], ')')
print('Thank you for connecting!')

while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
