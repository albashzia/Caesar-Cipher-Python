# creating a function to encrypt given text by shifting each alphabet by +3
def caesar_encrypt(text):
    shift = 3 # setting a default shift 
    encrypted_text = ""
    
    # looping over the whole given string
    for char in text:
        # dealing with lowercase alphabets
        if char.islower(): 
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            encrypted_text = encrypted_text + new_char
        # dealing with uppercase alphabets
        elif char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            encrypted_text = encrypted_text + new_char
        # dealing with characters other than alphabets
        else:
            encrypted_text = encrypted_text + char
    # returning the encrypted text
    return encrypted_text

# main program
message = input("Enter text to encrypt: ") # taking input from user
result = caesar_encrypt(message) # call to caesar encrypt function
print("Encrypted text:", result) # displaying encrypted text 
