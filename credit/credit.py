from cs50 import get_int

while True:
    int_number = get_int("Number: ")
    if int_number > 0:
        break

string_number = str(int_number)

if len(string_number) < 13 or len(string_number) > 16 or len(string_number) == 14:
    print("INVALID")

else:
    list_number = [string_number[n] for n in range(len(string_number))]
    list_all_numbers = []
    for number in list_number[-2::-2]:
        int_multiplication = int(number) * 2
        if int_multiplication > 9:
            string_multiplication = str(int_multiplication)
            for digit in string_multiplication:
                list_all_numbers.append(digit)
        else:
            string_multiplication = str(int_multiplication)
            list_all_numbers.append(string_multiplication)
    for number in list_number[::-2]:
        list_all_numbers.append(number)
    list_all_numbers_ints = []
    for number in list_all_numbers:
        list_all_numbers_ints.append(int(number))
    if sum(list_all_numbers_ints) % 10 != 0:
        print("INVALID")
    else:
        if len(string_number) == 15:
            print("AMEX")
        elif string_number[0:1] == '4':
            print("VISA")
        else:
            print("MASTERCARD")






