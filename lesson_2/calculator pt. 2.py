
""" 
This code takes 2 numbers, asks for an arithmetic value. 
and outputs the 2 numbers compared with the inputed value. 
"""


def prompt(message): 
    print(f"==> {message}")

def invalid_number(number_str): 
    try: 
        int(number_str)
    except ValueError: 
        return True 

    return False


prompt(' welcome to calculator')

prompt(' whats the first number?')
number1 = input()

while invalid_number(number1): 
    prompt("hmm..that doesn't look like a valid number.")
    number1 = input()

print(' whats the second number?')
number2 = input()

while invalid_number(number2): 
    prompt("hmm..that doesn't look like a valid number.")
    number2 = input()

print('what operation would you like to perform? \n 1.) add 2.) subtract 3.) multiply 4.) divide')
operation = input()

while operation not in ["1", "2", "3","4"]: 
    prompt('you must choose 1,2,3 or 4')
    operation = input()

match operation: 
    case '1': 
        output = int(number1) + int(number2)
    case '2': 
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(f' the result is: {output}')

