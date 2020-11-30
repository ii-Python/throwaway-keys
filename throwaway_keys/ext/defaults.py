# Modules
import hashlib

# Generators
generators = {
    # taken from https://docs.python.org/3.9/library/hashlib.html
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "shake128": hashlib.shake_128,
    "shake256": hashlib.shake_256,
    "sha3-224": hashlib.sha3_224,
    "sha3-256": hashlib.sha3_256,
    "sha3-384": hashlib.sha3_384,
    "sha3-512": hashlib.sha3_512,
    "blake2b": hashlib.blake2b,
    "blake2s": hashlib.blake2s
}