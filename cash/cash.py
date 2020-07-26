from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars > 0:
        break

quarters = 25
dimes = 10
nickels = 5
pennies = 1

cents = dollars * 100

number_of_quarters = cents // quarters
remainder1 = cents % quarters
number_of_dimes = remainder1 // dimes
remainder2 = remainder1 % dimes
number_of_nickels = remainder2 // nickels
remainder3 = remainder2 % nickels
number_of_pennies = remainder3 // pennies

addition = number_of_quarters + number_of_dimes + number_of_nickels + number_of_pennies

print(f"{addition:.0f}")
