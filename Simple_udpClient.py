from socket import *

def encrypt_vigenere(message, key):
    encrypted_message = ""
    key_length = len(key)

    for i in range(len(message)):
        char = message[i]
        key_char = key[i % key_length]
        if char.isalpha():
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char

    return encrypted_message

serverName = "192.168.15.50"
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("UDP Client\n")
while True:
    message = input("Input message: ")
    if message == "exit":
        break

    key = input("Vigenère key: ")
    encrypted_message = encrypt_vigenere(message, key)
    print("Encrypted message: " + encrypted_message)
    clientSocket.sendto(bytes(encrypted_message, "utf-8"), (serverName, serverPort))

clientSocket.close()
