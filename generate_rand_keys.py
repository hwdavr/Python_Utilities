import M2Crypto

def generate_rand_key(num_bytes):
    rand_bytes = M2Crypto.m2.rand_bytes(num_bytes)
    print(", ".join("0x{:02x}".format(ord(c)) for c in rand_bytes))


num_keys = 5
for i in range(0, num_keys):
    generate_rand_key(32)
    
    
