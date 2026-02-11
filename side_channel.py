import json
import subprocess
import time
import base64

runner = "./authenticator"

with open("ciphertext", "rb") as f:
    cipher = base64.b64encode(f.read()).decode()

def time_of_check(tag):
    payload = {
        "sender": "Bob",
        "receiver": "Alice",
        "data": cipher,
        "tag": tag
    }
    start = time.time()
    subprocess.run(
        [runner],
        input=json.dumps(payload).encode(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    total = time.time() - start
    return total

brute_tag = ""
length = 32

for i in range(length):
    times = {}
    runs = 5
    
    for j in range(256):
        tagger = brute_tag + f"{j:02x}"
        tagger += "00" * (length - i - 1)
        
        total_time = 0
        for _ in range(runs):
            total_time += time_of_check(tagger)
        times[j] = total_time / runs
    
    best = max(times, key=times.get)
    brute_tag += f"{best:02x}"
    print(f"recovered byte {i}: {best}")
    print(f"tag right now = {brute_tag}")

print(f"final {brute_tag}")