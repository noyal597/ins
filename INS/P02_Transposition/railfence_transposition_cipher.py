from math import ceil

def encrypt(text, key):
    rail = [['' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):

        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1
        row = row+1 if dir_down else row-1

    ciphertext = ''
    for i in range(len(rail)):
        for j in range(len(rail[i])):
            if rail[i][j] == '':
                continue
            ciphertext += rail[i][j]
    return ciphertext

def decrypt(ciphertext, key):
    rail = [['' for i in range(len(ciphertext))] for j in range(key)]
    dir_down = False
    length = len(ciphertext)
    cycle = 2 * (key - 1)
    k = ceil(length / cycle)
    row, col = 0, 0

    i = 0
    for row in range(key):
        for col in range(row, length, cycle):
            rail[row][col] = ciphertext[i]
            i += 1

    text = ''
    row = 0
    for col in range(length):
        text += rail[row][col]
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        row = row+1 if dir_down else row-1
    return text


print("0: Exit\n1: Encryption\n2: Decryption")
while True:
    match input("\nEnter your option: "):
        case '':
            pass
        case '0':
            print("Exiting...")
            break
        case '1':
            text = input("Enter text: ")
            key = int(input("Enter key value: "))
            print("\nEncrypted text: ", encrypt(text, key))
        case '2':
            text = input("Enter text: ")
            key = int(input("Enter key value: "))
            print("\nDecrypted text: ", decrypt(text, key))
        case _:
            print("Invalid Choise. Try again...")

