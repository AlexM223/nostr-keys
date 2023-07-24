# Keypair Generator

This Python script generates a cryptographic key pair using the secp256k1 elliptic curve, the same curve used by Bitcoin. 

The script generates a private key and corresponding public key, and then prints their hexadecimal representations.

## Dependencies

This script depends on the Python `secp256k1` library. You can install it using pip:

pip install secp256k1

shell
Copy code

## Usage

To run the script:

python keypair_generator.py

vbnet
Copy code

This will output a private key and public key in their hexadecimal forms.

## License

This project is licensed under the terms of the MIT License. For details, see the [LICENSE](LICENSE) file.

To get past the http problem on snort open the javascript console and typing “window.crypto.subtle = 1;” and then hitting enter.