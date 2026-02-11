import hashlib
import time
from memory_profiler import profile

@profile
def find_preimage():
    message = 0
    start = time.time()
    zero_bb = b"\x00" * 3

    while True:
        # change this to your wanted hash function
        hash = hashlib.sha3_256(str(message).encode())
        prefix = hash.digest()[:3]
        if prefix == zero_bb:
            endtime = time.time()
            print(f"preimage: {message} at: {prefix.hex()} full {hash.digest().hex()}")
            print(f"time: {endtime - start:.2f}")
            # remember to change this also
            break
        else:
            message += 1

if __name__ == "__main__":
    find_preimage()