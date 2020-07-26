from cs50 import get_string
from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    dictionary = open(argv[1], "r")

    message = get_string("What message would you like to censor?\n")

    list_message = message.split()

    list_dictionary = []

    for line in dictionary:
        strip_line = line.strip()
        list_dictionary.append(strip_line)

    list_censor = []

    for word in list_message:
        if word.lower() in list_dictionary:
            censor_word = "*" * len(word)
            list_censor.append(censor_word)
        else:
            list_censor.append(word)

    censor_message = " ".join(list_censor)
    print(censor_message)

    dictionary.close()

if __name__ == "__main__":
    main()