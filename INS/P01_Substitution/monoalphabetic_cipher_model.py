alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
chars = 'QWERTYUIOPASDFGHJKLZXCVBMN'
chars += chars.lower()

def encrypt(text):
    ciphertext = ''
    for char in text:
        if char in alphabets:
            char = chars[alphabets.index(char)]
        ciphertext += char
    return ciphertext

def decrypt(text):
    plaintext = ''
    for char in text:
        if char in chars:
            char = alphabets[chars.index(char)]
        plaintext += char
    return plaintext

if __name__ == "__main__":
    message = input("Enter message: ")
    ciphertext = encrypt(message)
    print("Encrypted Text:", ciphertext)
    plaintext = decrypt(ciphertext)
    print("Decrypted Text:", plaintext)

