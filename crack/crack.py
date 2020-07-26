import crypt
from sys import argv

if len(argv) != 2:
    print("Usage: python crack.py hash")
    exit(1)

elif len(argv[1]) != 13:
    print("Usage: python crack.py hash")
    exit(1)

password_hash = argv[1]

salt = password_hash[0:2]

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ'

for letter in alphabet:
    possible_hash = crypt.crypt(letter, salt)
    if possible_hash == password_hash:
        print(letter)
        exit(0)

for letter_1 in alphabet:
    for letter_2 in alphabet:
        list_word = [letter_1, letter_2]
        word = "".join(list_word)
        possible_hash = crypt.crypt(word, salt)
        if possible_hash == password_hash:
            print(word)
            exit(0)

for letter_1 in alphabet:
    for letter_2 in alphabet:
        for letter_3 in alphabet:
            list_word = [letter_1, letter_2, letter_3]
            word = "".join(list_word)
            possible_hash = crypt.crypt(word, salt)
            if possible_hash == password_hash:
                print(word)
                exit(0)

for letter_1 in alphabet:
    for letter_2 in alphabet:
        for letter_3 in alphabet:
            for letter_4 in alphabet:
                list_word = [letter_1, letter_2, letter_3, letter_4]
                word = "".join(list_word)
                possible_hash = crypt.crypt(word, salt)
                if possible_hash == password_hash:
                    print(word)
                    exit(0)

for letter_1 in alphabet:
    for letter_2 in alphabet:
        for letter_3 in alphabet:
            for letter_4 in alphabet:
                for letter_5 in alphabet:
                    list_word = [letter_1, letter_2, letter_3, letter_4, letter_5]
                    word = "".join(list_word)
                    possible_hash = crypt.crypt(word, salt)
                    if possible_hash == password_hash:
                        print(word)
                        exit(0)

print("can't crack this one :/")