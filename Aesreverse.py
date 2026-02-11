import hashlib

encrypted_message = bytes.fromhex('a7896ad1b2f7da8d40b33d1438e04a839a88b5c9a97625fe5017a5e1fb542072595d804d5ad1a3af11ea7244a39d76cde1')

plaintext = b'Move the tables to the patio as soon as possible!'
target =    b'Move the chairs to the house as soon as possible!'

print(plaintext)
print(list(plaintext))

print(target)
print(list(target))



print(len(encrypted_message))
print(len(plaintext))
print(len(target))



result = bytes(a ^ b ^ c for a, b, c, in zip(encrypted_message, plaintext, target))

print(result.hex())