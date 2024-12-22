a = int(input('what is the bill amount?'))
b = int(input('what is the tip percentage?'))

def calculation(x,y): 
    c = x * (y / 100)
    d = x + c
    print(f'the tip is ${c}')
    print(f'the toal is ${d}')

calculation(a,b)