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

message = input("Enter text to decrypt: ")
result = caesar_decrypt(message)
print("Decrypted text:", result)
