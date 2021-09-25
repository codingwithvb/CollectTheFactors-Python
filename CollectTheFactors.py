number = input("What is the Number?")
number_value = int(number)

number_array = []

number1 = number_value % 1

if number1 == 0:
  number_array.append(1)

number2 = number_value % 2

if number2 == 0:
  number_array.append(2)

number3 = number_value % 3

if number3 == 0:
  number_array.append(3)

number4 = number_value % 4

if number4 == 0:
  number_array.append(4)

number5 = number_value % 5

if number5 == 0:
  number_array.append(5)

number6 = number_value % 6

if number6 == 0:
  number_array.append(6)

number7 = number_value % 7

if number7 == 0:
  number_array.append(7)

number8 = number_value % 8

if number8 == 0:
  number_array.append(8)

print(number_array)

prime_number = len(number_array)

if prime_number <= 2:
  print("Prime Number")
