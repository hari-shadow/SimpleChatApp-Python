import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection to server closed.")
            break

def send_messages():
    while True:
        message = input()
        
        if message.startswith('@'):
            recipient, private_message = message[1:].split(' ', 1)
            client_socket.send(message.encode('utf-8'))
        else:
            client_socket.send(message.encode('utf-8'))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5555))

initial_prompt = client_socket.recv(1024).decode('utf-8')
print(initial_prompt, end='')
username = input()
client_socket.send(username.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

