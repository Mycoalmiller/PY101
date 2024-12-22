
import random 

name = input('what is your name?')

if name == ' ' or "" or len(name) == 0:
    name = 'Teddy' 

def age(a):
    b = random.randint(20,100)
    return (f"{name} is {b} years old!")

print(age(a))