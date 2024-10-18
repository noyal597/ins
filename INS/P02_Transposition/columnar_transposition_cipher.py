import math


def encrypt(text, key):
    columns = len(key)
    order = {k: i for i, k in enumerate(key)}
    table = [text[i:i+columns] for i in range(0, len(text), columns)]

    ciphertext = ""
    for column in sorted(order.keys()):
        try:
            for row in range(len(table)):
                ciphertext += table[row][order[column]]
        except IndexError:
            ciphertext += '\0'  # null charecter
    return ciphertext


def decrypt(ciphertext, key):
    columns = len(key)
    sorted_key = sorted(key)

    plaintext = ""
    rows = math.ceil(len(ciphertext) / columns)
    for i in range(rows):
        for k in key:
            plaintext += ciphertext[(sorted_key.index(k) * rows) + i]
    return plaintext.replace('\0', '')


if __name__ == '__main__':
    text = "HERE-IS-SOME-TEXT"
    key = "3124"

    ciphertext = encrypt(text, key)
    print("Encrypted message: ", ciphertext)
    plaintext = decrypt(ciphertext, key)
    print("Decrypted message: ", plaintext)
