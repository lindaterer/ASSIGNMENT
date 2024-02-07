import random

substitution_mapping = {
    'g': 'q',
    'i': 'x',
    'r': 'a',
    'l': 'p',
}


plain_text = "girl"

encrypted_text = ""


for char in plain_text:
    
    encrypted_char = substitution_mapping.get(char, char)
    encrypted_text += encrypted_char

print("Plain Text:  ", plain_text)
print("Encrypted Text:", encrypted_text)
