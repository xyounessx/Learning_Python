import random

number = random.randrange(1, 100, 1)
print(number)

attempts = 5

for i in range(0, attempts):
    user_input = input('Please enter a number: ')
    if user_input.isdigit():
        if int(user_input) != number:
            print('Wrong!')
        else:
            break
    else:
        print('Its not a number!')
print('Correct!')