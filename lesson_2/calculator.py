print('=> welcome to calculator')

print('=> whats the first number?')
number1 = input()
print('=> whats the second number?')
number2 = input()

print('what operation would you like to perform? \n 1.) add 2.) subtract 3.) multiply 4.) divide')
operation = input()

if operation == '1': 
    output = int(number1) + int(number2)
elif operation == '2': 
    output = int(number1) - int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
    output = int(number1) / int(number2)

print(f' the result is: {output}')