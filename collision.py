import hashlib
import time
from memory_profiler import profile

@profile
def find_collision():
    message = 0
    kaikki = {}
    start = time.time()

    while True:
        # change this to your wanted hash function
        hash = hashlib.md5(str(message).encode())
        prefix = hash.digest()[:4]
        if prefix in kaikki:
            endtime = time.time()
            print(f"collision: {kaikki[prefix]} with {message} at: {prefix.hex()}")
            print(f"time: {endtime - start:.2f}")
            # remember to change this also
            hash2 = hashlib.md5(str(kaikki[prefix]).encode())
            print(f"full hashes: {hash.digest().hex()}, {hash2.digest().hex()}")
            break
        else:
            kaikki[prefix] = message
            message += 1

if __name__ == "__main__":
    find_collision()