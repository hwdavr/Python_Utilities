import binascii
from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256

def encrypt_AES_CBC(msg, secretKey, iv):
    aesCipher = AES.new(secretKey, AES.MODE_CBC, iv)
    ciphertext = aesCipher.encrypt(msg)
    return ciphertext

def hmac_sha256(msg, macKey):
    hmac = HMAC.new(macKey, msg, SHA256)
    return hmac.digest()

def print_nice_bytearray(hex_array):
    print(", ".join("0x{:02x}".format(c) for c in hex_array))

def print_nice_bytes(hex_array):
    print(", ".join("0x{:02x}".format(ord(c)) for c in hex_array))
    
    
