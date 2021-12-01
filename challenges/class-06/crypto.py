from cryptography.fernet import Fernet


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


def encrypt():
    message = input("Input message to encrypt: ")
    message_encoded = message.encode()
    # initialize the Fernet class
    f = Fernet(key)
    # encrypt the message
    encrypted = f.encrypt(message_encoded)
    print("Message encrypted:")
    print(encrypted)


def decrypt():
    message = input("Input message to decrypt: ")
    message_encoded = str.encode(message)
    f = Fernet(key)
    # decrypt the message
    decryped = f.decrypt(message_encoded)
    print("Drecrypted message: " + str(decryped))


def encrypt_file():
    f = Fernet(key)
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
    f = Fernet(key)
    file = input("Enter filepath for file decryption? ")
    with open(file, "rb") as file:
        # read the encrypted data
        encrypted = file.read()
    # decrypt data
    decrypted_info = f.decrypt(encrypted)
    # write the original file
    with open(file, "wb") as file:
        file.write(decrypted_info)


def bring_meu():
    mode = input(
        "\nMake a selection: \n1 - Encrypt a file \n2 - Decrypt a file \n3 - Encrypt a message \n4 - Decrypt a message \n")
    if (mode == "1"):
        encrypt_file()
    elif (mode == "2"):
        decrypt_file()
    elif (mode == "3"):
        encrypt()
    elif (mode == "4"):
        decrypt()
    elif ((mode != "1") and (mode != "2") and (mode != "3") and (mode != "4")):
        print("Select a valid option:\n")


def menu_loop():
    choice = "y"
    while True:
        bring_meu()
        choice = input("Try again? y/n ")
        if choice == "n" or "N" or "no" or "NO":
            print("\nThank you!")
            break


def start():
    menu_loop()


write_key()
key = load_key()

start()
