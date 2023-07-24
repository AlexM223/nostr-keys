import os
import binascii
from secp256k1 import PrivateKey

def generate_keypair():
    private_key = PrivateKey()
    public_key = private_key.pubkey
    return private_key, public_key

def keypair_to_hex(private_key, public_key):
    private_key_hex = binascii.hexlify(private_key.private_key).decode()
    public_key_hex = binascii.hexlify(public_key.serialize()).decode()
    return private_key_hex, public_key_hex

private_key, public_key = generate_keypair()
private_key_hex, public_key_hex = keypair_to_hex(private_key, public_key)

print("Private Key:", private_key_hex)
print("Public Key:", public_key_hex)
