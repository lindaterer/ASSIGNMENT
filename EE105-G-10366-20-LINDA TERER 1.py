def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
    
            is_upper = char.isupper()
            shifted_char = chr(((ord(char) - ord('A' if is_upper else 'a') + shift) % 26) + ord('A' if is_upper else 'a'))
            
            encrypted_text += shifted_char
        else:
        
            encrypted_text += char
    
    return encrypted_text

plain_text = "girl"
shift = 3
encrypted_text = caesar_cipher(plain_text, shift)
print("Plain Text:  ", plain_text)
print("Encrypted Text:", encrypted_text)
