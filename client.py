import socket, sys, time

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socet.gethostname(server_host)
sport = 8080

print("This is your IP address: ", ip)
server_host = input("Enter friend's IP address:")
name = input("Enter friend's name: ")

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.rcv(1024)
server_name = server_name.decode()

print(server_name, " has joined...")
while True:
  message = (socket_server.recv(1024)).decode()
  print(server_name, ":", message)
  message = input("Me: ")
  socket_server.send(message.encode())
  
