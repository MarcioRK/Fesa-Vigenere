from socket import *

def decrypt_vigenere(encrypted_message, key):
    decrypted_message = ""
    key_length = len(key)

    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[i % key_length]
        if char.isalpha():
            shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        else:
            decrypted_char = char
        decrypted_message += decrypted_char

    return decrypted_message

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("UDP server\n")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    encrypted_text = str(message, "utf-8")
    key = input("Vigenère key: ")
    decrypted_message = decrypt_vigenere(encrypted_text, key)
    print("Received: ", encrypted_text)
    print("Decrypted Message: ", decrypted_message)
