## PyChat - Real-time Chat Application in Python

PyChat is a simple real-time chat application implemented in Python using socket programming. This project provides a basic chat server that allows multiple clients to connect, communicate, and exchange messages in real-time.

### Features:

- **User Authentication:** Clients are prompted to enter a unique username upon connection.
- **Broadcast Messages:** Send messages that are broadcasted to all connected clients.
- **Private Messaging:** Use the '@username' syntax to send private messages to specific users.
- **User Join/Leave Notifications:** Inform users when someone joins or leaves the chat.

### How to Use:

1. Clone the repository: `git clone https://github.com/hari-shadow/PyChat.git`
2. Run the server: `python chat_server.py`
3. Open multiple terminals and run clients: `python chat_client.py`
4. Enter a unique username for each client and start chatting.
