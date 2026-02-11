R = 0xe1000000000000000000000000000000
MASK = 0xffffffffffffffffffffffffffffffff

def gf_mul(x, y):
    z = 0
    v = x
    for i in range(128):
        if (y >> (127 - i)) & 1:
            z ^= v
        if v & 1:
            v = (v >> 1) ^ R
        else:
            v >>= 1
    return z & MASK

def gf_pow(x, e):
    r = x
    for _ in range(e - 1):
        r = gf_mul(r, x)
    return r


# H from Task 3.1
H = int("4636bdbd1c7643d34ee4bb1bf9ca084f", 16)

# Verify short cycle
print("H^5 == H:", gf_pow(H, 5) == H)
print("H^4 == 1:", gf_pow(H, 4) == 1)
