import socket

s = socket.socket()
s.bind(('127.0.0.1', 54321))
s.listen(1)
while true:
  client, addr = s.accept()
  while true:
    content = client.recv(32)
    if len(content) ==0:
      break
    else:
      print(content)
print("client disconnected\n")
client.close()
    
  
