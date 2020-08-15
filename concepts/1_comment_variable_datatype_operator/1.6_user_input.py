# input function helps to take user input from keyboard to our program, entered input is always of string data type
name = input('Enter your name:')

age = input('Enter your age:')
print(type(age)) # The output will be str even though we entered int value because input function always takes string

print('{} you are {} years old'.format(name,age))