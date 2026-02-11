from Crypto.Cipher import AES
import os

msg_block1 = b'Sixteen byters16'
msg_block2 = b'Sixteen byters16'    
plaintext = msg_block1 + msg_block2

key = os.urandom(16)
iv = os.urandom(16)

cipher1 = AES.new(key, AES.MODE_ECB)
ciphertext1 = cipher1.encrypt(plaintext)

cipher2 = AES.new(key, AES.MODE_CBC, iv)
ciphertext2 = cipher2.encrypt(plaintext)

cipher3 = AES.new(key, AES.MODE_CTR)
ciphertext3 = cipher3.encrypt(plaintext)
nonce = cipher3.nonce

print(ciphertext1.hex())
print(ciphertext2.hex())
print(ciphertext3.hex())
