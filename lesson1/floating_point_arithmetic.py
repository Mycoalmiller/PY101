a = float(input('first number:'))
b = float(input('second number:'))


def math(x,y):
    index = 0
    c = [x+y, x-y, x*y, x/y, x//y, x%y, x**y]
    d = ['+','-','*','/','//','&','**']
    while index < len(c) and len(d):
        result = c[index]
        print(f'{a} {d[index]} {b} = {result}')
        index += 1

math(a,b)