from Crypto.Cipher import AES


key = b"This is crazyman"

message = b"some message"

cipher = AES.new(key, AES.MODE_GCM)

ciphertext, tag = cipher.encrypt_and_digest(message)

one_tag = tag[:1]

message2 = 0

while True:
    cipher2 = AES.new(key, AES.MODE_GCM, cipher.nonce)
    ciphertext, tag2 = cipher2.encrypt_and_digest(message2.to_bytes())

    if tag2[:1] == one_tag:
        print(f"collision at {message2} when tag1 {one_tag} and tag2 {tag2[:1]} equal")
        break
    message2 += 1