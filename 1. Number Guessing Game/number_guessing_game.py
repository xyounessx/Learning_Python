import random

number = random.randrange(1, 100, 1)
# print(number)

while True:
    user_input = input('Please enter a number: ')
    if user_input.isdigit():
        if int(user_input) < 10 or int(user_input) > 100:
            print('Its not a number btween 10-100')
        continue
    else:
        print('Its not a number!')
        continue
    break