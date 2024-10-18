p = 5
q = 7
privkey1 = 3
privkey2 = 4

print("The value of P is %s" %p,
      "The value of Q is %s" %q,
      "Private key for Alice is %s" %privkey1,
      "Private Key for Bob is %s" %privkey2,
      sep='\n')

pubkey1 = int(pow(p, privkey1, q))
pubkey2 = int(pow(p, privkey2, q))

print("\nPublic Key for Alice is %s" %pubkey1,
      "Public Key for Bob is %s" %pubkey2,
      sep='\n')

key1 = int(pow(pubkey2, privkey1, q))
key2 = int(pow(pubkey1, privkey2, q))
print("\nSecret number for Alice is %s:" %key1,
      "Secret number for Bob is %s" %key2,
      sep='\n')

