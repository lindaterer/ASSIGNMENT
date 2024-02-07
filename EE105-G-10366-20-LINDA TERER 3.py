def create_vigenere_square():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_square = {}
    for i, char in enumerate(alphabet):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        vigenere_square[char] = shifted_alphabet
    return vigenere_square

def vigenere_encrypt(plain_text, key):
    vigenere_square = create_vigenere_square()
    encrypted_text = ""
    key_repeated = key * (len(plain_text) // len(key)) + key[:len(plain_text) % len(key)]

    for i in range(len(plain_text)):
        plain_char = plain_text[i]
        key_char = key_repeated[i]
        
        if plain_char.isalpha():
            is_upper = plain_char.isupper()
            shifted_alphabet = vigenere_square[key_char.upper()]
            shift = ord('A' if is_upper else 'a')
            encrypted_char = shifted_alphabet[ord(plain_char) - shift]
            encrypted_text += encrypted_char if is_upper else encrypted_char.lower()
        else:
            encrypted_text += plain_char

    return encrypted_text

plain_text = "girl"
key = "lady"
encrypted_text = vigenere_encrypt(plain_text, key)
print("Plain Text:  ", plain_text)
print("Key:         ", key)
print("Encrypted Text:", encrypted_text)
