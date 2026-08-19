import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server is waiting for connection...")

conn, address = server_socket.accept()
print("Connected to:", address)

message = conn.recv(1024).decode()
print("Message from client:", message)

response = "Message received successfully by the server."
conn.send(response.encode())

conn.close()
server_socket.close()