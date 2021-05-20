import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostname(host_name)
port = 8080

new_socket.bind((host_name, port))
print("Binding successfull!")
print("This is your IP:", s_ip)

name = input("Enter name:")
new_socket.listen(1)

conn, add = new_socket.accept()
print("Recieved connection from", add[0])
print("Connection established. Connected from: ", add[0])

client = (conn.recv(1024)).decode()
print(client + " has connected")
conn.send(name.encode())
while True:
  message = input("Me: ")
  conn.send(message.encode())
  message = conn.recv(1024)
  message = message.decode()
  print(client, ':', message)

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
