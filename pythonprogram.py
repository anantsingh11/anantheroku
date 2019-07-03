import socket

s = socket.socket()
print("Socket successfully created")
port = 11223
s.bind(('', port))
print("socket binded to %s" %port)
s.listen(5)
print("socket is listening")
conn, addr = s.accept()
with conn:
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

    c.send('data= I am SERVER\n')
c.close()
    
  
