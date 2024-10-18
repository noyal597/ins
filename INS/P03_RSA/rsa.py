import binascii
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
pubkey = key.publickey()
print("\n:: Public Key :-\nn = %s\ne = %s" % (pubkey.n, pubkey.e))

pubkeyPEM = pubkey.exportKey()
print("\n:: Public Key PEM :-", pubkeyPEM.decode('ascii'), sep='\n')

print("\n:: Private Key :-\nn = %s\ne = %s" % (key.n, key.e))

privkeyPEM = key.exportKey()
print("\n:: Private Key PEM :-", privkeyPEM.decode('ascii'), sep='\n')

msg = "message"  # input("Enter a message: ")

encryptor = PKCS1_OAEP.new(pubkey)
ciphertext = encryptor.encrypt(msg.encode('UTF-8'))
print("\n:: Cipher Text :-", binascii.hexlify(ciphertext), sep='\n')

decryptor = PKCS1_OAEP.new(key)
plaintext = decryptor.decrypt(ciphertext)
print("\n:: Plain Text :-", plaintext.decode('UTF-8'), sep='\n')
