from cs50 import get_string
from cs50 import get_int
from sys import argv


if len(argv) != 2:
    print("Usage: python vigenere.py k")
    exit(1)

for symbol in argv[1]:
    if symbol.isalpha() == False:
        print("Usage: python vigenere.py k")
        exit(1)

k = argv[1]

plaintext = get_string("plaintext: ")

list_ascii_cipher_letters = []
list_alphabet_cipher_letters = []
list_key = []
key_index = 0

for k_letters in k:
    if k_letters.islower() == True:
        k_upper_letters = k_letters.upper()
        ascii_k_upper_letters = ord(k_upper_letters)
        key = ascii_k_upper_letters - 65
        list_key.append(key)

    else:
        ascii_k_letters = ord(k_letters)
        key = ascii_k_letters - 65
        list_key.append(key)

for plain_letters in plaintext:
    if plain_letters.isupper() == True:
        ascii_upper_plain_letters = ord(plain_letters)
        ascii_upper_cipher_letters = (((ascii_upper_plain_letters - 65) + list_key[key_index]) % 26) + 65
        list_ascii_cipher_letters.append(ascii_upper_cipher_letters)
        key_index = (key_index + 1) % len(list_key)

    elif plain_letters.islower() == True:
        ascii_lower_plain_letters = ord(plain_letters)
        ascii_lower_cipher_letters = (((ascii_lower_plain_letters - 97) + list_key[key_index]) % 26) + 97
        list_ascii_cipher_letters.append(ascii_lower_cipher_letters)
        key_index = (key_index + 1) % len(list_key)

    else:
        ascii_plain_letters = ord(plain_letters)
        list_ascii_cipher_letters.append(ascii_plain_letters)

for cipher_letters in list_ascii_cipher_letters:
    alphabet_cipher_letters = chr(cipher_letters)
    list_alphabet_cipher_letters.append(alphabet_cipher_letters)

ciphertext = "".join(list_alphabet_cipher_letters)

print(f"ciphertext: {ciphertext}")