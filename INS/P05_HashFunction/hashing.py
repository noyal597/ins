import hashlib
text = input("Enter some text: ")
text_hash = hashlib.sha1(text.encode())
print("The hexadecimal equivalent of SHA1 is", text_hash.hexdigest())
