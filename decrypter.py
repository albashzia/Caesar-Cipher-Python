# creating a function to decrypt given text by shifting each alphabet by -3
def caesar_decrypt(text):
    shift = 3  # setting a default shift 
    decrypted_text = ""
    # looping over the whole given string
    for char in text:
         # dealing with lowercase alphabets
        if char.islower():
            position = ord(char) - ord('a')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('a'))
            decrypted_text = decrypted_text + new_char
        # dealing with uppercase alphabets
        elif char.isupper():
            position = ord(char) - ord('A')
            new_position = (position - shift) % 26
            new_char = chr(new_position + ord('A'))
            decrypted_text = decrypted_text + new_char
         # dealing with characters other than alphabets
        else:
            decrypted_text = decrypted_text + char
    # returning the decrypted text
    return decrypted_text

# main 
message = input("Enter text to decrypt: ") # taking input from user
result = caesar_decrypt(message) # call to caesar decrypt function
print("Decrypted text:", result)  # displaying decrypted text 
