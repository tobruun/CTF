from Crypto.Cipher import Salsa20

string = b"winner winner chicken dinner"
string2 = b"winner winner chicken dinnar"

key = b"*Thirty-two byte (256 bits) key*"
key2 = b"Jaajo Linnonmaa on aamujuontaja!"
nonce = b"12345678"

cipher = Salsa20.new(key, nonce)
cipher2 = Salsa20.new(key2, nonce)

ciphertext = cipher.nonce + cipher.encrypt(string)
ciphertext2 = cipher2.nonce + cipher2.encrypt(string2)

print(ciphertext.hex())
print(ciphertext2.hex())