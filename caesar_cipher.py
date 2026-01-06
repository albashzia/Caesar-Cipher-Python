def caesar_encrypt(text):
    shift = 3
    encrypted_text = ""
    for char in text:
        if char.islower():
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            encrypted_text = encrypted_text + new_char
        elif char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            encrypted_text = encrypted_text + new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text):
    shift = 3
    decrypted_text = ""
    for char in text:
        if char.islower():
            position = ord(char) - ord('a')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('a'))
            decrypted_text = decrypted_text + new_char
        elif char.isupper():
            position = ord(char) - ord('A')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('A'))
            decrypted_text = decrypted_text + new_char
        else:
            decrypted_text = decrypted_text + char
    return decrypted_text

print("Welcome to Caesar Cipher Encrypter & Decrypter")
choice = ""
while choice != "3":
    print("Menu: ")
    print("1. Encrypt a text.")
    print("2. Decrypt a text.")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter the text: ")
        result = caesar_encrypt(text)
        print("Encrypted Text :",result)
        print()

    elif choice == "2":
        text = input("Enter the text: ")
        result = caesar_decrypt(text)
        print("Decrypted Text :",result)
        print()

    elif choice == "3":
        break

    else:
        print("Invalid Choice.\nTo perform an operation enter 1 or 2, to exit enter 3.")
        print()
