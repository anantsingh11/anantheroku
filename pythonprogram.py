import socket
import sys
import os
from _thread import *

host = '0.0.0.0'
#port = 11223
port = int(os.getenv('PORT', 11223))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for connection\n ')
def threaded_client(conn):
    conn.send(str.encode('WELCOME, Type your data\n'))

    while True:
        data = conn.recv(4096)
        reply = 'server output: ' +data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print('connected to: ' +addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client(conn,))
    
  
