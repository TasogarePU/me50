from cs50 import get_string
from cs50 import get_int
from sys import argv


if len(argv) != 2:
    print("Usage: python caesar.py k")
    exit(1)

for symbol in argv[1]:
    if symbol.isdigit() == False:
        print("Usage: python caesar.py k")
        exit(1)

if int(argv[1]) <= 0:
    print("Usage: python caesar.py k")
    exit(1)

k = int(argv[1])

plaintext = get_string("plaintext: ")

list_ascii_cipher_letters = []
list_alphabet_cipher_letters = []

for plain_letters in plaintext:
    if plain_letters.isupper() == True:
        ascii_upper_plain_letters = ord(plain_letters)
        ascii_upper_cipher_letters = (((ascii_upper_plain_letters - 65) + k) % 26) + 65
        list_ascii_cipher_letters.append(ascii_upper_cipher_letters)

    elif plain_letters.islower() == True:
        ascii_lower_plain_letters = ord(plain_letters)
        ascii_lower_cipher_letters = (((ascii_lower_plain_letters - 97) + k) % 26) + 97
        list_ascii_cipher_letters.append(ascii_lower_cipher_letters)

    else:
        ascii_plain_letters = ord(plain_letters)
        list_ascii_cipher_letters.append(ascii_plain_letters)

for cipher_letters in list_ascii_cipher_letters:
    alphabet_cipher_letters = chr(cipher_letters)
    list_alphabet_cipher_letters.append(alphabet_cipher_letters)

ciphertext = "".join(list_alphabet_cipher_letters)

print(f"ciphertext: {ciphertext}")