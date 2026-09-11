print('Hello World!')

x = input('Please enter your name: ')
print(x)
### check what type of input is entered by user
if x.isalpha():
    print('It is a string!')
elif x.isdigit():
    print('It is an integer!')