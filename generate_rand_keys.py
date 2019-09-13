import os, binascii

def generate_rand_key(num_bytes):
    rand_bytes = os.urandom(num_bytes)
    print(", ".join("0x{:02x}".format((c)) for c in rand_bytes))

num_keys = 1
for i in range(0, num_keys):
    generate_rand_key(320)
    
    
