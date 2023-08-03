import os
import binascii
from secp256k1 import PrivateKey
import bech32

def generate_keypair():
    private_key = PrivateKey()
    public_key = private_key.pubkey
    return private_key, public_key

def keypair_to_hex(private_key, public_key):
    private_key_hex = binascii.hexlify(private_key.private_key).decode()
    public_key_hex = binascii.hexlify(public_key.serialize()).decode()
    return private_key_hex, public_key_hex

def encode_data(hrp, data):
    # Custom encoding function to encode only the data part
    data_int = bech32.convertbits(data, 8, 5)
    return bech32.bech32_encode(hrp, data_int)

def private_key_to_nsec(private_key_hex):
    private_key_bytes = bytes.fromhex(private_key_hex)
    nsec_hrp = "nsec"
    nsec_version = 0
    nsec_encoded = encode_data(nsec_hrp, private_key_bytes)
    return nsec_encoded

private_key, public_key = generate_keypair()
private_key_hex, public_key_hex = keypair_to_hex(private_key, public_key)

print("Private Key:", private_key_hex)
print("Public Key:", public_key_hex)

nsec_key = private_key_to_nsec(private_key_hex)
print("NSEC Key:", nsec_key)
