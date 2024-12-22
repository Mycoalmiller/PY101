
def triangle(a): 
    index = 0
    while index < a: 
        print((' ' * (-abs(index) + (a-1))) + ('*' * abs(index + 1)))
        index += 1