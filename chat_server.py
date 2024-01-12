import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    client_socket.send("Enter your username: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')
    
    broadcast(f"{username} has joined the chat.", address)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            if message.startswith('@'):
                recipient, private_message = message[1:].split(' ', 1)
                send_private_message(username, recipient, private_message)
            else:
                broadcast(f"{username}: {message}", address)

        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break

    broadcast(f"{username} has left the chat.", address)

    print(f"Connection from {address} closed")

def broadcast(message, sender_address):
    for client, address, _ in clients:
        if address != sender_address:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client, address)

def send_private_message(sender, recipient, message):
    for client, address, username in clients:
        if username == recipient:
            try:
                client.send(f"Private message from {sender}: {message}".encode('utf-8'))
                break
            except:
                remove_client(client, address)

def remove_client(client, address):
    print(f"Connection from {address} closed unexpectedly")
    for c, a, _ in clients:
        if c == client:
            clients.remove((c, a, _))
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen(5)

print("Server listening on port 5555")

clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append((client_socket, client_address, ''))

    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()

