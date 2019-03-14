import binascii
from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto.Hash import SHA256

hexstr = "00000000000000000000000000000000"

enc_key = "5555555555555555555555555555555555555555555555555555555555555555"
mac_key = "5555555555555555555555555555555555555555555555555555555555555555"
iv = "00000000000000000000000000000000"

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
    
    
hex_bytes = binascii.unhexlify(hexstr)
print("plain data length ", len(hex_bytes))
print_nice_bytes(hex_bytes)

enc_bytes = binascii.unhexlify(enc_key)
print("ENC key length ", len(enc_bytes))
print_nice_bytes(enc_bytes)

cipher_data = encrypt_AES_CBC(hex_bytes, enc_bytes, binascii.unhexlify(iv))
print("cipher data length ", len(cipher_data))
print_nice_bytes(cipher_data)

mac_data = hmac_sha256(cipher_data, binascii.unhexlify(mac_key))
print("MAC data length ", len(mac_data))
print_nice_bytes(mac_data)
