import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print(word)

user_guess = ''
turns = 12

while turns > 0:
    for char in word:
        if char in user_guess:
            print(char, end=' ')
        else:
            print('_', end=' ')

    guess = input("Guess a character: ").lower()
    user_guess += guess

    if len(user_guess) != 1:
        print('enter a single character!')
        continue

    if user_guess == word:
        print('You won!')
        break