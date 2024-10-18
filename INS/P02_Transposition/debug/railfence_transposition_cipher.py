from math import ceil

def rail_fence_encrypt(text, key):
    rail = [['' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):

        if (row == 0) or (row == key - 1):
            print("\nreverse dir_down = %s" % (dir_down))
            dir_down = not dir_down

        print("\n%s = '%s'" % (i, text[i]))
        rail[row][col] = text[i]
        print("row = %s, col = %s" % (row, col))
        print(rail[0])
        print(rail[1])
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    ciphertext = ''
    for i in range(len(rail)):
        for j in range(len(rail[i])):
            if rail[i][j] == '':
                continue
            ciphertext += rail[i][j]
    return ciphertext

def rail_fence_decrypt(ciphertext, key):
    rail = [['' for i in range(len(ciphertext))] for j in range(key)]
    dir_down = False
    length = len(ciphertext)
    cycle = 2 * (key - 1)
    k = ceil(length / cycle)
    print(k)
    row, col = 0, 0
    print("Cycle value: ", cycle)
    print("total rows = %s, cols = %s" % (len(rail), len(rail[0])))

    i = 0
    for row in range(key):
        for col in range(row, length, cycle):
            print("\nrow = %s, col = %s" % (row, col))
            rail[row][col] = cipher[i]
            i += 1
            print(rail[0])
            print(rail[1])

    text = ''
    row = 0
    for col in range(length):
        text += rail[row][col]
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        if dir_down:
            row += 1
        else:
            row -= 1
    return text


key = 2
cipher = rail_fence_encrypt("HAPPY BIRTHDAY", key)
print("\n\nEncrypted text:- ", cipher)
print("===================================\n\n")
text = rail_fence_decrypt(cipher, key)
print("\n\nDecrypted text:- ", text)

