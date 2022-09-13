import socket
import random

print("---Client---")

HOST, PORT = "127.0.0.1", 3003  # -> 1 to 65535
LIST = ["rock", "paper", "scissors"]
client_choice = random.choice(LIST)
print(f"My choice is {client_choice}")
print("Wait for Server ...")

# socket.AF_INET     -> Internet Address Familly for IPv4
# socket.SOCK_STREAM -> Socket Type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(client_choice.encode())
    print(client_socket.recv(2048).decode())
