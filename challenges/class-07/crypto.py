from cryptography.fernet import Fernet
import os
import math
import time


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


def check_key():
    key = load_key()
    if key == None:
        key = write_key()
        return Fernet(key)


def encrypt():
    message = input("Input message to encrypt: ")
    message_encoded = message.encode()
    # initialize the Fernet class
    f = check_key()
    # encrypt the message
    encrypted = f.encrypt(message_encoded)
    print("Message encrypted:")
    print(encrypted)


def decrypt():
    message = input("Input message to decrypt: ")
    message_encoded = str.encode(message)
    f = check_key()
    # decrypt the message
    decryped = f.decrypt(message_encoded)
    print("Drecrypted message: " + str(decryped))


def encrypt_file():
    f = check_key()
    file = input("Enter filepath for file encryption: ")
    with open(file, "rb") as file:
        # read file data
        file_data = file.read()
    # encrypt data
    encrypted_file = f.encrypt(file_data)
    # write the encrypted file
    with open(file, "wb") as file:
        file.write(encrypted_file)


def decrypt_file():
    f = check_key()
    file = input("Enter filepath for file decryption? ")
    with open(file, "rb") as file:
        # read the encrypted data
        encrypted = file.read()
    # decrypt data
    decrypted_info = f.decrypt(encrypted)
    # write the original file
    with open(file, "wb") as file:
        file.write(decrypted_info)


def re_encrypt(file):
    f = check_key()
    with open(file, "rb") as file:
        data = file.read()
        encrypted = f.encrypt(data)
        with open(file, "wb") as file:
            file.write(encrypted)


def re_decrypt(file):
    f = check_key()
    with open(file, "rb") as file:
        encrypted = file.read()
    decrypted = f.decrypt(encrypted)
    with open(file, "wb") as file:
        file.write(decrypt)


def encrypt_dir():
    path = input("Enter path to the directory to encrypt: ")
    for (path, dirs, files) in os.walk(path):
        for file in files:
            file_name = os.path.join(path, file)
            re_encrypt(file_name)


def decrypt_dir():
    path = input("Enter path to the directory to decrypt: ")
    for (path, dirs, files) in os.walk(path):
        for file in files:
            file_name = os.path.join(path, file)
            re_decrypt(file_name)


def bring_menu():
    mode = input(
        "\nMake a selection: \n1 - Encrypt a file \n2 - Decrypt a file \n3 - Encrypt a message \n4 - Decrypt a message \n5 - Encrypt a folder \n6 - Decrypt a folder\n")
    if (mode == "1"):
        encrypt_file()
    elif (mode == "2"):
        decrypt_file()
    elif (mode == "3"):
        encrypt()
    elif (mode == "4"):
        decrypt()
    elif (mode == "5"):
        encrypt_dir()
    elif (mode == "6"):
        decrypt_dir()
    else:
        print("\nPlease select a valid option!\n")
        bring_menu()


def menu_loop():
    choice = "y"
    while True:
        bring_menu()
        choice = input("Try again? y/n ")
        if choice == "n" or "N" or "no" or "NO":
            print("\nThank you!")
            break


def start():
    menu_loop()


write_key()
key = load_key()

start()

# source: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
