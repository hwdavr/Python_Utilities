from base64 import b64decode 
from base64 import b64encode
import ecdsa
import os, binascii
from Crypto.Hash import SHA256

#github: https://kjur.github.io/jsrsasign/sample/sample-ecdsa.html
message = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIDEzIGxhenkgZG9ncy4="
public_key = "f75beec0b9de18780b9052d166b7d325f45665aa45b782ece53aa98c60fc5835bd43251d8f7db19a7da05d8f88f40e7426443ed9d589e1adc9f920319eb9c830"
signature = "bec6f4cfa858acc026843909773405e07f1f7631ada7c4ee31e02496278a1b326fc52ab4b7e3eab7d3291e180d26ee365fe1254521b3b46ab7551eb89181e392"

# Get public key
# vk = ecdsa.VerifyingKey.from_pem((public_key))
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.NIST256p)
# Calcualte digest
digest = SHA256.new() 
digest.update((message.encode('utf-8')))
print(binascii.hexlify((digest.digest())))

verified = vk.verify_digest(bytes.fromhex(signature), digest.digest())
assert verified, 'Signature verification failed'

