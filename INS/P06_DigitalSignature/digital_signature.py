from binascii import hexlify
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
pubkey = key.publickey()

original_data = b"This is original docuemt."
modified_data = b"This is modified docuemt."

original_hash = SHA256.new(original_data)
modified_hash = SHA256.new(modified_data)

signature = pkcs1_15.new(key).sign(original_hash)
print(hexlify(signature))

try:
    pkcs1_15.new(pubkey).verify(original_hash, signature)
    print("Valid Signature")
except (ValueError, TypeError):
    print("Invalid Signature")
