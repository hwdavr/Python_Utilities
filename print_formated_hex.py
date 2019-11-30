import os, binascii
import sys


hex_string = sys.argv[1]
hex_bytes = binascii.unhexlify(hex_string)
print(", ".join("0x{:02x}".format((c)) for c in hex_bytes))

    
    
