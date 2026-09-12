import random

number = random.randint(1, 100)

attemps = 7

for i in range(0, attemps):
    print(f'attemp [{i+1}] out of [{attemps}]')
    while True:
        user_input = input('Please enter a number: ')
        if user_input.isdigit():
            user_number = int(user_input)
            break
        else:
            print('Your input is not a number!')
    if user_number > number:
        print('Too big!')
    elif user_number < number:
        print('Too small!')
    else:
        print('You won!')
        break
else:
    print(f'You lost! The number was: {number}')