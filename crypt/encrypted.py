from sys import argv
from cs50 import get_string
import crypt

if len(argv) != 2:
    print("Usage: python encrypted.py salt")

if len(argv[1]) != 2:
    print("Usage: python encrypted.py salt")

salt = argv[1]

key = get_string("key: ")

encrypted = crypt.crypt(key, salt)

print(f"hash: {encrypted}")