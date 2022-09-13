import socket
import random

print("---Server---")

HOST, PORT = "127.0.0.1", 3003  # -> 1 to 65535
LIST = ["rock", "paper", "scissors"]
server_choice = random.choice(LIST)
print(f"My choice is {server_choice}")
print("Wait for Client ...")

# socket.AF_INET     -> Internet Address Familly for IPv4
# socket.SOCK_STREAM -> Socket Type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    con_socket, ret_address = server_socket.accept()
    with con_socket:
        client_choice = con_socket.recv(2048).decode()
        msg = f"SERVER picked: {server_choice}\nCLIENT picked: {client_choice}"
        if server_choice == client_choice:
            msg += "\nDRAW"
        elif server_choice == "rock" and client_choice == "paper":
            msg += "\nWinner is [Client]"
        elif server_choice == "rock" and client_choice == "scissors":
            msg += "\nWinner is [Server]"
        elif server_choice == "paper" and client_choice == "rock":
            msg += "\nWinner is [Server]"
        elif server_choice == "paper" and client_choice == "scissors":
            msg += "\nWinner is [Client]"
        elif server_choice == "scissors" and client_choice == "paper":
            msg += "\nWinner is [Server]"
        elif server_choice == "scissors" and client_choice == "rock":
            msg += "\nWinner is [Client]"

        print(msg)
        con_socket.sendall(msg.encode())
